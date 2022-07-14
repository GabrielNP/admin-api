import uuid
from datetime import date
from typing import Union

class UserRole:
    def __init__(self, data):
        self.user_role_id: uuid = data['user_role_id'].hex
        self.role_id: uuid = data['role_id']
        self.user_id: uuid = data['user_id']
        self.project_id: uuid = data['project_id']
        self.created_at: date = data['created_at'].isoformat()
        self.updated_at: date = data['updated_at'].isoformat()
        self.deleted_at: Union[date, None] = data['deleted_at']
    
    def serialize(self):
        del self.deleted_at
        return self.__dict__
