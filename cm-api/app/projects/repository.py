from flask import current_app as app
from sqlalchemy import text

from app.projects.project import Project


def search_by_name(name: str) -> Project:
    with app.config['DB'].connect() as conn:
        data = conn.execute(
            text("""
                SELECT *
                FROM projects
                WHERE name = :name
                AND deleted_at IS NULL
            """), name=name)
        data = data.fetchone()
        return Project(data) if data else None

def insert(data: Project) -> Project:
    with app.config['DB'].connect() as conn:
        data = conn.execute(
            text("""
                INSERT INTO projects 
                (name) VALUES (:name)
                RETURNING *
            """), name=data['name']
        )
        data = data.fetchone()
        return Project(data) if data else None

