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

def get_user_roles(user_id: str):
     with app.config['DB'].connect() as conn:
        data = conn.execute(
            text("""
            SELECT roles.name
            FROM roles
            JOIN user_roles ur ON ur.role_id = roles.role_id
            AND ur.deleted_at IS NULL
            WHERE ur.user_id = :userid
            AND roles.deleted_at IS NULL
            """), userid=user_id)
        data = data.fetchall()
        print(data)
        return [dict(d) for d in data] if data else []
