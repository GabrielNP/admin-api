import uuid
from datetime import date


class User:
    def __init__(self, data):
        self.user_id = data['user_id'].hex
        self.name = data['name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at'].isoformat()
        self.updated_at = data['updated_at'].isoformat()
        self.deleted_at = data['deleted_at']

    def serialize(self):
        del self.password
        del self.deleted_at
        return self.__dict__
