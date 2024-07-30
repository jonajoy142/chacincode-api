import asyncio
from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from starlette import status
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from app.db.connectivity import check_db_connection
from app.config.network_connectivity import validate_network, load_network_profile
from app.models.defaultResModel import DefaultResponse
from app.helpers.limiter import limiter
import app.db.schemas as schemas
from app.db.connectivity import engine
from scalar_fastapi import get_scalar_api_reference
from app.constants.app_constants import AppConsts
from app.routers.sample_router import sample_router
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create all schemas in the database
schemas.db_base.metadata.create_all(bind=engine)

# Create FastAPI instance
app = FastAPI(
    title=AppConsts.NAME,
    description=AppConsts.DESCRIPTION,
    version=AppConsts.VERSION
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rate limiter setup
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# Dependency to validate network connectivity
async def validate_network_dependency() -> bool:
    try:
        client = load_network_profile("app/config/network.json")
        await asyncio.get_event_loop().run_in_executor(None, validate_network, client)
        return True
    except Exception as e:
        logger.error(f"Network validation failed: {str(e)}")
        return False

# Root route - checks both database and network connectivity
@app.get(path="/")
@limiter.limit(limit_value='1/second')
async def get_root(
        request: Request,
        can_connect_db: bool = Depends(check_db_connection),
        can_connect_network: bool = Depends(validate_network_dependency)
        ) -> DefaultResponse:
    '''
    Root route of API. Gives response according to database and network connectivity.
    :param request: Request model from FastAPI, for rate limiter
    '''
    if can_connect_db and can_connect_network:
        return DefaultResponse(message="Database and network connected",
                               data={'can_connect_db': can_connect_db, 'can_connect_network': can_connect_network})
    
    if not can_connect_db:
        logger.error("Database connectivity failed")
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Database connectivity failed",
            headers={'Retry-After': "30"}
        )

    if not can_connect_network:
        logger.error("Network connectivity failed")
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Network connectivity failed",
            headers={'Retry-After': "30"}
        )

# Documentation route
@app.get("/newdocs", include_in_schema=False)
async def scalar_html():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title=app.title
    )

# Include other routers
app.include_router(router=sample_router)
