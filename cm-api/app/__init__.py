import logging
import os

from dotenv import load_dotenv
from flask import Blueprint, Flask, request
from flask.helpers import make_response
from sqlalchemy import create_engine

from app.auth.handler import auth_bp
from app.projects.handler import project_bp
from app.users.handler import user_bp


load_dotenv()

app = Flask(__name__)
app.config['DB'] = create_engine(os.getenv('DATABASE_URL'), client_encoding='utf8', implicit_returning=True)
app.config['SERVER'] = 'CM_ADMIN_API'
app.logger.setLevel(logging.INFO)

api = Blueprint('api', __name__, url_prefix='/api')

api.register_blueprint(auth_bp)
api.register_blueprint(project_bp)
api.register_blueprint(user_bp)
app.register_blueprint(api)


@app.errorhandler(400)
def bad_request(error):
    return make_response({'detail': 'Bad Request', 'error_code': 400}), 400

@app.errorhandler(404)
def not_found(error):
    print(error)
    return make_response({'detail': 'Not Found', 'error_code': 404}), 404

@app.errorhandler(405)
def server_error(error):
    return make_response({'detail': 'Method Not Allowed', 'error_code': 405}), 405

@app.errorhandler(500)
def server_error(error):
    return make_response({'detail': 'Server Error', 'error_code': 500}), 500

@app.before_request
def handle_requests():
    from app.middleware import Middleware
    from app.pkg import response

    
    middleware = Middleware(app, request)
    if not middleware.authorize():
        return response.unauthorized()
