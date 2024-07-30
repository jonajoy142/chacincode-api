from starlette import status
from pydantic import BaseModel, SkipValidation
from typing import Dict


class DefaultResponse(BaseModel):
    class Config:
        arbitrary_types_allowed = True
    status_code: int = 200
    api_status: str = 'UP'
    message: str = 'OK'
    data: Dict = {}
    status: SkipValidation = status.HTTP_200_OK
