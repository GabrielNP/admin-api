import uuid
from datetime import datetime
from typing import Union


class Project:
    def __init__(self,data):
        self.project_id: uuid = data['project_id']
        self.name: str = data['name']
        self.created_at: datetime = data['created_at']
        self.updated_at: datetime = data['updated_at']
        self.deleted_at: Union[datetime, None] = data['deleted_at']

    def serialize(self):
        return self.__dict__
