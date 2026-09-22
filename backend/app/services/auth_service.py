from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.security import verify_password
from app.models import User

def authenticate_user(
    db:Session,
    email:str,
    password:str
)-> User:
    
    user = db.scalar(
        select(User).where(User.email == email)
    )
    if not user:
        raise ValueError("Invalid email or password")
   
    if not verify_password(password,user.password_hash):
        raise ValueError("Invalid email or password")

    if not user.is_active:
        raise ValueError("User Account is Inactive!")

    return user