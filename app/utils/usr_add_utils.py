from typing import Type
import uuid
from sqlalchemy.orm import Session
from starlette import status
from app.constants.custom_message import ERROR_WHILE_ADDING_DATA
from app.db.schemas import SampleTable
from app.exceptions.custom_exception import CustomException
from app.models.defaultResModel import DefaultResponse
from app.models.usr_add_req_model import UsrAddReqModel


def add_user(user: UsrAddReqModel, db: Session) -> DefaultResponse:
    new_user: Type[SampleTable] = add_user_to_sample_tb(name=user.name, db=db)
    return DefaultResponse(
        api_status="Data added successfully",
        message="User added to database",
        data=new_user.to_dict()
    ).model_dump()


def add_user_to_sample_tb(name: str, db: Session) -> Type[SampleTable]:
    user: Type[SampleTable] = SampleTable()
    user.name = name
    user.unique_id = get_unique_id(data=name)

    try:
        db.add(user)
        db.commit()

        db.refresh(user)

        if not user.id:
            raise CustomException(code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                                  message=ERROR_WHILE_ADDING_DATA)
        return user
    except Exception as e:
        raise CustomException(code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                              message=str(e))


def get_unique_id(data: str) -> str:
    """
    create unique id for the user
    Args:
        data (str): user name

    Returns:
        str: unique id
    """
    # delete whitespace
    data = data.replace(" ", "")
    # make it upper
    data = data.upper()
    # genered a unique suffix of 3 character
    suffix = str(uuid.uuid4().int)[:3]
    return data+suffix
