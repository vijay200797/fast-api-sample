

from pydantic import BaseModel, validate_email, field_validator, Field

class People(BaseModel):
    age:int
    name: str