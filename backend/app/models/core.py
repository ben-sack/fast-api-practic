from pydantic import BaseModel


class CoreModel(BaseModel):
    """
    Any common logic to be inherited
    """


class IDModelMixing(BaseModel):
    id: int
