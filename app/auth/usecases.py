from app.auth.auth import Login
from app.pkg import crypt, jwt
from app.users import repository as user_repo
from app.users.user import User
from app.user_roles.user_role import UserRole
from app.user_roles import repository as user_role_repo


def login_uc(data) -> Login:
    user: User = user_repo.search_by_email(data['email'])
    if not user:
        raise Exception('invalid username or password')

    raw_psswd = crypt.Crypt(str.encode(data['password'])).decrypt()

    if not crypt.check_hash(raw_psswd, str.encode(user.password)):
        raise Exception('invalid username or password')

    access_token, refresh_token = jwt.encode_token(user.user_id)

    data = Login(data={
        'user_id': user.user_id,
        'access_token': access_token,
        'refresh_token': refresh_token,
        'roles': [],
        'admin': user.is_admin
    })

    if user.is_admin:
        return data.serialize()

    user_roles: UserRole = user_role_repo.list(user.user_id)
    data.roles = [f"{item['project_id']}.{item['role_id']}" for item in user_roles]

    return data.serialize()
