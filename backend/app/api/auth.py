from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models import User
from app.api.dependencies import get_current_user
from app.schemas.auth import RegisterRequest, UserResponse, LoginRequest, TokenResponse
from app.services.user_service import create_user
from app.services.auth_service import authenticate_user
from app.core.security import create_access_token


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
)
def register(
    data: RegisterRequest,
    db: Session = Depends(get_db),
):
    try:
        user = create_user(db, data)

    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(exc),
        )

    return UserResponse(
        id=user.id,
        full_name=user.full_name,
        email=user.email,
        phone=user.phone,
        role=user.role.name,
        is_active=user.is_active,
    )

@router.post(
    "/login",
    response_model = TokenResponse,
)
def login(
    data: LoginRequest,
    db:Session = Depends(get_db)
):
    try:
        user = authenticate_user(
            db,
            data.email,
            data.password,
        )
    except ValueError as exc:
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail=str(exc)
        )
    access_token = create_access_token(
        user_id = user.id,
        role = user.role.name,
    )

    return TokenResponse(
        access_token=access_token,
        token_type = "bearer",
    )

@router.get("/me", response_model=UserResponse)
def get_me(
    current_user: User = Depends(get_current_user)
):
    return UserResponse(
        id = current_user.id,
        full_name = current_user.full_name,
        email = current_user.email,
        phone = current_user.phone,
        role = current_user.role.name,
        is_active = current_user.is_active,
    )
    
    