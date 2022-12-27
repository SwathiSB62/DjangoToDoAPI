import dataclasses
from typing import TYPE_CHECKING
from . import models


if TYPE_CHECKING:
    from . models import User

@dataclasses.dataclass
class UserDataClass:
    email: str
    password: str = None
    created_timestamp: str = None
    updated_timestamp: str = None
    id: int = None

    @classmethod
    def from_instance(cls, user:"User" )->"UserDataClass":
        return cls(
            email=user.email,
            id=user.id,
            created_timestamp=user.created_timestamp,
            updated_timestamp=user.updated_timestamp
        )

def create_user(user_dc: "UserDataClass") -> "UserDataClass":
    instance = models.User(
        email=user_dc.email        
    )
    if user_dc.password is not None:
        instance.set_password(user_dc.password)
    instance.save()
    return UserDataClass.from_instance(instance)
