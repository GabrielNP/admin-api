from flask import current_app as app
from sqlalchemy import text

from app.users.user import User

def list():
    with app.config['DB'].connect() as conn:
        data = conn.execute("SELECT * FROM users")
        data = data.fetchall()
        return [User(dict(d)).serialize() for d in data]

def search_by_id(email: str) -> User:
    with app.config['DB'].connect() as conn:
        data = conn.execute(
            text("""
                SELECT *
                FROM users
                WHERE email = :email
                AND deleted_at IS NULL
            """),
            email=email
        )
        data = data.fetchone()
        return User(data) if data else None

def get_by_id(id: str) -> User:
    with app.config['DB'].connect() as conn:
        data = conn.execute(
            text("""
                SELECT *
                FROM users
                WHERE user_id = :id
                AND deleted_at IS NULL
            """),
            id=id
        )
        data = data.fetchone()
        return User(data) if data else None
