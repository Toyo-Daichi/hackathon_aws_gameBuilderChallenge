from ..util.logger import Logger
logging = Logger(__name__, "INFO")

class GameState:
    _instance = None
    _initialized: bool
    state: str
    mode: str
    score: int

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            logging.info("Creating a new instance")
            cls._instance = super(GameState, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if getattr(self,'_initialized', False):
            return 
        self._initialize()

    def _initialize(self):
        self.state = "START"
        self.mode = "Normal"
        self._initialized = True
        self.score = 0

    def get_state(self):
        return self.state

    def get_mode(self):
        return self.mode

    def get_score(self):
        return self.score

    def set_state(self, state: str):
        self.state = state

    def set_mode(self, mode: str):
        self.mode = mode
    
    def set_score(self, score: int):
        self.score = score
