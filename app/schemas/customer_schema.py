from pydantic import BaseModel

class CustomerSchema(BaseModel):                 
    name: str
    unique_id: str
    class Config:
        orm_mode = True
