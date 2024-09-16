from fastapi import Depends, HTTPException, status

from app.auth.user_db import UserDB
from app.models.user import UserDto
from fastapi.security import OAuth2PasswordBearer
from app.mock.fake_user_db import fake_users

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")  # use token authentication

def api_key_auth(token: str = Depends(oauth2_scheme)) -> UserDto:

    for user_from_db in fake_users:
        user = UserDB(**user_from_db)
        if user.token == token and user.isActive:
            return UserDto(**user_from_db)

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Forbidden"
    )