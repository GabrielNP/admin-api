from app.pkg.exceptions import MissingDataException, ForbiddenException


def create(data):
    if 'name' not in data or not data['name']:
        raise MissingDataException('name')

def list(user_id: str):
    from app.users import repository as user_repo
   
    user_id: str = "2af1b9e0-2541-4949-b483-5ed8f9d47650"
    user = user_repo.get_by_id(user_id)
    if not user:
        raise ForbiddenException
