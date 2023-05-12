from fastapi import FastAPI
from jose import jwt
from pydantic import BaseModel
from datetime import datetime, timedelta

SECRET_KEY = "e0945f09d29c8b563347fdfe355329c0db379ff3f4adcc26b2f3d525d95b2ba8"
ALGORITHM = "HS256"


class Token(BaseModel):
    access_token: str
    token_type: str


app = FastAPI()

to_encode = ''


def create_access_token(data: dict):
    to_encode = data
    expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_token(token):
    try:
        jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except:
        print("Error")
