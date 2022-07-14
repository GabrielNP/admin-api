from flask.blueprints import Blueprint

from app.users import repository as user_repo
from app.pkg import response

user_bp = Blueprint('user_bp', __name__, url_prefix='/users')

@user_bp.route('/', methods=['GET'])
def list():
    users = user_repo.list()
    return response.list(users)
