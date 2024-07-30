
from urllib.request import Request
from app.db.connectivity import get_db
from app.models.usr_add_req_model import UsrAddReqModel
from fastapi import APIRouter, Depends, HTTPException
from app.models.addProduct_request_model import ProductAddRequest
from app.models.defaultResModel import DefaultResponse
from app.services.chaincode_services import add_product_to_ledger
from app.exceptions.custom_exception import CustomException

sample_router = APIRouter(
    prefix="/api/v1",
    tags=['Blockchain Operations']
)

@sample_router.post("/add-product", response_model=DefaultResponse)
async def add_product(request: ProductAddRequest):
    try:
        print(request.dict(), "HERE 1")
        response = await add_product_to_ledger(request.dict())
        return DefaultResponse(message="Product added successfully", data=response)
    except CustomException as ce:
        raise HTTPException(status_code=500, detail=str(ce))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")



# add new sample user
# @sample_router.post(path='/add/user', name="Add sample user")
# # @limiter.limit(limit_value='1/second')
# async def add_new_user(request: Request,
#                        request_body: UsrAddReqModel,
#                        db: Session = Depends(get_db)):
#     """
#     add a sample user to the database
#     Args:
#         request (Request): want this variable to activate the limiter
#         request_body (_type_): request body - pydantic model.
#         db (Session): database session. Defaults to Depends(get_db).
#     """
#     try:
#         response: DefaultResponse = add_user(user=request_body, db=db)
#         return response
#     except CustomException as ce:
#         raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
#                             detail=str(ce))
