from flask import Request


UNAUTHORIZED_ROUTES = [
    "/api/auth",
    "/api/auth/encrypt"
]

class Middleware:
    def __init__(self, app, request: Request):
        self.app = app
        self.request = request

    def authorize(self) -> bool:
        if self.request.path in UNAUTHORIZED_ROUTES:
            return True

        if self.request.headers and not self.request.headers.get("Authorization"):
            return False
