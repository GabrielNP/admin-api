from app.auth.auth import Login
from app.pkg import authorization, crypt
from app.pkg.exceptions import ForbiddenException
from app.user_roles import repository as user_role_repo
from app.user_roles.user_role import UserRole
from app.users import repository as user_repo
from app.users.user import User


def login_uc(data) -> Login:
    user: User = user_repo.search_by_email(data['email'])
    if not user:
        raise Exception('invalid username or password')

    raw_psswd = crypt.Crypt(str.encode(data['password'])).decrypt()

    if not crypt.check_hash(raw_psswd, str.encode(user.password)):
        raise Exception('invalid username or password')

    if user.is_admin:
        user_roles = []
    else:
        user_roles = user_role_repo.get_user_roles(user.user_id)
        if len(user_roles) == 0:
            raise ForbiddenException()

    access_token, refresh_token, expiration = authorization.generate_token(user.user_id, user_roles, admin=user.is_admin)

    data = Login(data={
        'user_id': user.user_id,
        'access_token': access_token,
        'refresh_token': refresh_token,
        'roles': [],
        'admin': user.is_admin
    })


    return data.serialize()
