from context.api import API
from model.api.user import UserEntity

END_POINT = "/users"

class User:
    api: API

    def __init__(self):
        self.api = API()
