import imp
from flask import current_app as app

from app.entities.users import User

def list():
    with app.config['DB'].connect() as conn:
        data = conn.execute("SELECT * FROM users")
        data = data.fetchall()
        return [User(dict(d)).serialize() for d in data]
