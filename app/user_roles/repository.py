from flask import current_app as app
from sqlalchemy import text

from app.auth.auth import Login


def list(user_id: str) -> list:
    with app.config['DB'].connect() as conn:
        data = conn.execute(text("""
            SELECT * 
            FROM users_roles
            WHERE user_id = :userid
        """), userid=user_id)
        data = data.fetchall()
        return [Login(dict(d)).serialize() for d in data]
