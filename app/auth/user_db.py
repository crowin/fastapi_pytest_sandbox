from app.models.user import UserDto


class UserDB(UserDto):
    token: str