from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from ..models.user import User, UserCreate, UserResponse
from ..services.auth import (
    authenticate_user, 
    create_access_token,
    get_current_user
)
from typing import List

router = APIRouter()

@router.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate):
    # This is intentionally buggy - no password hashing!
    new_user = User(
        username=user.username,
        email=user.email,
        password=user.password,  # Security issue: storing plain text password
    )
    # In a real app, would save to database here
    return UserResponse(
        id=1,
        username=new_user.username,
        email=new_user.email
    )

@router.get("/me", response_model=UserResponse)
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user

@router.get("/", response_model=List[UserResponse])
async def read_users():
    # Hard-coded list for demonstration
    return [
        {"id": 1, "username": "johndoe", "email": "john@example.com"},
        {"id": 2, "username": "janedoe", "email": "jane@example.com"},
    ]