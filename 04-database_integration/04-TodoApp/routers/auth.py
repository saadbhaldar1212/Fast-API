from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from jose import jwt
from datetime import timedelta, datetime

from validate import CreateUserRequest
from models import User
from database import SessionLocal

router = APIRouter()

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

SECRET_KEY = "9fbaaf4db609eee260a4363d0e94c2b985edd982dc2b01999fb541eb7d5ea966"
ALGORITHM = "HS256"


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


def authenticate_user(username: str, password: str, db):
    user = db.query(User).filter(User.username == username).first()
    if not user and not bcrypt_context.verify(password, user.hashed_password):
        return False
    return user


def create_access_token(username: str, user_id: int, expires_delta: timedelta):
    encode = {
        "sub": username,
        "id": user_id,
    }
    expire = datetime.utcnow() + expires_delta
    encode.update({"exp": expire})

    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)


db_dependency = Annotated[Session, Depends(get_db)]
oauth_dependency = Annotated[OAuth2PasswordRequestForm, Depends()]


@router.get("/read_all_users", status_code=status.HTTP_200_OK)
async def read_all_users(db: db_dependency):
    return db.query(User).all()


@router.post("/auth/create_user", status_code=status.HTTP_201_CREATED)
async def create_user(db: db_dependency, validate: CreateUserRequest):
    user_model = User(
        email=validate.email,
        username=validate.username,
        first_name=validate.first_name,
        last_name=validate.last_name,
        role=validate.role,
        hashed_password=bcrypt_context.hash(validate.hashed_password),
        is_active=True,
    )

    db.add(user_model)
    db.commit()


@router.post("/token")
async def login_for_access_token(form_data: oauth_dependency, db: db_dependency):
    user = authenticate_user(form_data.username, form_data.password, db)

    if not user:
        return "Failed Authentication"
    token = create_access_token(user.username, user.id, timedelta(minutes=20))
    return token
