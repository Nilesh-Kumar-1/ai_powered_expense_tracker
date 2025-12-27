from pydantic import BaseModel, EmailStr

class UserCreateRequest(BaseModel):
    username: str
    email: EmailStr
    first_name: str
    last_name: str
    password: str
    role: str
    first_name: str = ""
    last_name: str = ""
    is_active: bool = True