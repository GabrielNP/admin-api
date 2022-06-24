import uuid
from datetime import date
from typing import Union


class User:
    def __init__(self, data):
        self.user_id: uuid = data['user_id'].hex
        self.name: str = data['name']
        self.email = data['email']
        self.password: str = data['password']
        self.created_at: date = data['created_at'].isoformat()
        self.updated_at: date = data['updated_at'].isoformat()
        self.deleted_at: Union[date, None] = data['deleted_at']
        self.is_active: bool = data['is_active']

    
    def serialize(self):
        del self.password
        del self.deleted_at
        return self.__dict__
