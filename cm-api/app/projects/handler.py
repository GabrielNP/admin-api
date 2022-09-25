from http import HTTPStatus
from flask import Blueprint, request

from app.pkg import response
from app.projects import usecases
from app.projects import validators


project_bp = Blueprint('project_bp', __name__, url_prefix='/projects')

@project_bp.route('', methods=['POST'])
def create():
    try:
        data = request.get_json()
        validators.create(data)
        project = usecases.create(data)
        return response.success('project successfully created', project)
    except Exception as e:
        return response.error(f'{e}', 'fail to create project')

@project_bp.route('', methods=['GET'])
def list():
    from app.pkg.exceptions import ForbiddenException
    from app.projects import usecases

    try:
        authorization_token = request.headers.get("Authorization")
        # TODO: Decode token to get user
        validators.list(authorization_token['user_id'])
        projects = usecases.list(authorization_token['user_id'])
        return response.success('projects successfully listed', projects)
    except Exception as e:
        if isinstance(e, ForbiddenException):
            return response.error('forbidden', 'fail to list projects', HTTPStatus.FORBIDDEN)
        return response.error(f'{e}', 'fail to list projects')
