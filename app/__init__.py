import logging
import os

from dotenv import load_dotenv
from flask import Flask
from flask.helpers import make_response
from sqlalchemy import create_engine

from app.users.handler import user_bp


load_dotenv()

app = Flask(__name__)
app.config['DB'] = create_engine(os.getenv('DATABASE_URL'), client_encoding='utf8', implicit_returning=True)
app.logger.setLevel(logging.INFO)

app.register_blueprint(user_bp)

@app.errorhandler(400)
def bad_request(error):
    return make_response({"detail": "Bad Request", "error_code": 400}), 400

@app.errorhandler(404)
def not_found(error):
    return make_response({"detail": "Not Found", "error_code": 404}), 404

@app.errorhandler(405)
def server_error(error):
    return make_response({"detail": "Method Not Allowed", "error_code": 405}), 405

@app.errorhandler(500)
def server_error(error):
    return make_response({"detail": "Server Error", "error_code": 500}), 500
