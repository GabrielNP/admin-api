import uuid
from dataclasses import dataclass
from datetime import date


@dataclass
class Role(object):
    role_id: uuid.UUID
    name: str
    description: str
    created_at: date
    updated_at: date
    deleted_at: date
