from pydantic import BaseModel

class SystemUserSchema(BaseModel):
    username: str
    password: str

    class Config:
        orm_mode = True