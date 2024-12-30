import os
#
from .db import Db

class GameState:
    _instance = None
    _initialized: bool

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(GameState, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if getattr(self,'_initialized', False):
            return
        self._initialize()

    def _initialize(self):
        pass
