from pydantic import BaseModel


class UsrAddReqModel(BaseModel):
    """
    user adding request model for /add/user route
    Args:
        BaseModel (_type_): pydantic model
    """
    name: str
