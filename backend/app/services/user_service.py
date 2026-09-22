from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.security import hash_password
from app.models import Role, User
from app.schemas.auth import RegisterRequest


def create_user(
    db: Session,
    data: RegisterRequest,
) -> User:

    existing_user = db.scalar(
        select(User).where(User.email == data.email)
    )

    if existing_user:
        raise ValueError("Email is already registered")

    user_role = db.scalar(
        select(Role).where(Role.name == "USER")
    )

    if not user_role:
        raise ValueError("USER role does not exist")

    user = User(
        role_id=user_role.id,
        full_name=data.full_name,
        email=data.email,
        phone=data.phone,
        password_hash=hash_password(data.password),
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user