# Pydantic imports
from pydantic import BaseModel, EmailStr, Field


# Models
class User(BaseModel):
    email: EmailStr = Field(..., title='Email')
    firstname: str = Field(..., title="First_name")
    lastname: str = Field(..., title='Last_name')
    password: str = Field(..., title="Password")


