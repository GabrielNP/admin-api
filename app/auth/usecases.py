from app.pkg import crypt
from app.users import repository as user_repo
from app.users.user import User


def login_uc(data) -> User:
    user: User = user_repo.search_by_email(data['email'])
    if not user:
        raise Exception('invalid username or password')

    raw_psswd = crypt.Crypt(str.encode(data['password'])).decrypt()

    if not crypt.check_hash(raw_psswd, str.encode(user.password)):
        raise Exception('invalid username or password')

    return user.serialize()
