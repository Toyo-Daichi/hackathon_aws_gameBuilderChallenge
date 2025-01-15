import os
import psycopg2
from psycopg2.extensions import connection
#
from util.logger import Logger
logging = Logger(__name__, "INFO")

class DbEntity:
    reader_host: str
    writer_host: str
    port: int
    db_name: str
    user_name: str
    password: str

    def __init__(self):
        self.reader_host = os.getenv("READER_HOST", "localhost")
        self.writer_host = os.getenv("WRITER_HOST", "localhost")
        self.port = 5432
        self.db_name = os.getenv("DB_NAME", "gameday")
        self.db_user = os.getenv("DB_USER", "appuser")
        self.password = os.getenv("PASSWORD", "password")

class Db:
    _instance = None
    _initilized: bool
    db_entity: DbEntity 
    pool: connection

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Db, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if getattr(self, '_initilized', False):
            return
        self._initilize()

    def _initilize(self):
        self.db_entity = DbEntity()
        self._initilized = True
        self._connect(True)

    def _connect(self, use_writer=False):
        host = self.db_entity.writer_host \
            if use_writer \
            else self.db_entity.reader_host
        
        try:
            self.pool = psycopg2.connect(
                host = host,
                port = self.db_entity.port,
                dbname = self.db_entity.db_name,
                user = self.db_entity.db_user,
                password = self.db_entity.password,
            )
            logging.info(f"database connection successful ({host})")
        
        except Exception as e:
            logging.critical(f"Miss connecting to the database: {e}")
            raise e

    def get_pool(self):
        return self.pool
