import uuid

class Login:
    def __init__(self, data):
        self.user_id: uuid = data['user_id']
        self.access_token: str = data['access_token']
        self.refresh_token: str = data['refresh_token']
        self.admin: bool = data['admin']
        self.roles: list = data['roles']

    def serialize(self):
        return self.__dict__
