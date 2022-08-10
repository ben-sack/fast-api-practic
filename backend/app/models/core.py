from pydantic import BaseModel


class CoreModel(BaseModel):
    """
    Any common logic to be inherited
    """

    class Config:
        use_enum_values = True
        arbitrary_types_allowed = True


class IDModelMixin(BaseModel):
    id: int
