from pydantic import BaseModel
import uuid
from datetime import datetime

class User(BaseModel):
    uid: uuid.UUID
    name: str
    email: str
    password: str
    created_at: datetime
    update_at: datetime

class UserCreateModel(BaseModel):
    name: str
    email: str
    password: str

class UserUpdateModel(BaseModel):
    name: str
    email: str
    password: str