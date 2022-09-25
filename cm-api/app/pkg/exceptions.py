class MissingDataException(Exception):
    """Exception raised when some data is missing in a request.

    Attributes:
        field -- field that is missing
    """

    def __init__(self, field: str):
        self.field = field
        self.message: str = f'{field} is missing or empty'
        super().__init__(self.message)

class EntityNotFound(Exception):
    """Exception raised when some entity is not found.
    Ex: user not found

    Atributes:
        entity -- entity that was not found
    """

    def __init__(self, entity: str):
        self.message: str = f'{entity} not found'
        super().__init__(self.message)

class ForbiddenException(Exception):
     """Exception raised when api receive forbiden calls.
    Ex: valid authorization token but containing invalid user_id
    """

     def __init__(self):
        super().__init__()
