from flask import current_app as app
from sqlalchemy import text

from app.users.user import User

def list():
    with app.config['DB'].connect() as conn:
        data = conn.execute("SELECT * FROM users")
        data = data.fetchall()
        return [User(dict(d)).serialize() for d in data]

def search_by_email(email: str) -> User:
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
