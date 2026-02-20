from fastapi import Depends, status, HTTPException, APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from app.core.auth import Token, authenticate_user, create_access_token
from app.core.auth import fake_users_db, ACCESS_TOKEN_EXPIRE_MINUTES
from typing import Annotated
from datetime import timedelta
from app.core import auth as auth_core
from app.schemas.user import UserCreate, UserOut

router = APIRouter(tags=["Authentication"])


@router.post("/signup", response_model=UserOut, status_code=201)
async def signup(user_in: UserCreate):
    try:
        user = auth_core.create_user(user_in.dict())
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    # Note: persistence to DB is not implemented yet.
    return user


@router.post("/login")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()], # pyright: ignore[reportInvalidTypeForm]
) -> Token:
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")
