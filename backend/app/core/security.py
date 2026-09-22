from pwdlib import PasswordHash
from datetime import datetime, timedelta, timezone

import jwt
from jwt.exceptions import PyJWTError

from app.core.config import settings


password_hash = PasswordHash.recommended()


def hash_password(password: str) -> str:
    return password_hash.hash(password)


def verify_password(
    password: str,
    hashed_password: str,
) -> bool:
    return password_hash.verify(
        password,
        hashed_password,
    )
def create_access_token(
    user_id: int,
    role: str,
) -> str:
    expire = datetime.now(timezone.utc) + timedelta(
        minutes=settings.access_token_expire_minutes
    )

    payload = {
        "sub": str(user_id),
        "role": role,
        "exp": expire,
    }

    token = jwt.encode(
        payload,
        settings.secret_key,
        algorithm=settings.algorithm,
    )

    return token

def decode_access_token(token:str) -> dict:
    try:
        payload = jwt.decode(
            token,
            settings.secret_key,
            algorithms = [settings.algorithm]
        )
        return payload
    except PyJWTError:
        raise ValueError("Invalid or expired token")
         
    