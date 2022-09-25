import uuid
from datetime import datetime
from typing import Union


class User:
    def __init__(self, data):
        self.user_id: uuid = data['user_id'].hex
        self.name: str = data['name']
        self.email = data['email']
        self.password: str = data['password']
        self.created_at: datetime = data['created_at'].isoformat()
        self.updated_at: datetime = data['updated_at'].isoformat()
        self.deleted_at: Union[datetime, None] = data['deleted_at']
        self.is_active: bool = data['is_active']
        self.is_admin: bool = data['is_admin']

    
    def serialize(self):
        del self.password
        del self.deleted_at
        return self.__dict__
