from app.projects.project import Project
from app.projects import repository

def create(data) -> Project:
    project: Project = repository.search_by_name(data['name'])
    if project:
        raise Exception('invalid project name')
    
    project = repository.insert(data)

    return project.serialize()
