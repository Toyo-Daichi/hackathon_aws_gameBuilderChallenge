import requests
from typing import Generic, TypeVar, Dict, Any, Optional

from util.logger import Logger
logging = Logger(__name__, "INFO")

T = TypeVar('T')
R = TypeVar('R')

class API:
    _instance = None
    _initialized: bool
    session: requests.Session
    timeout: int
    url: str

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            logging.info("Creating a new instance")
            cls._instance = super(API, cls).__new__(cls)
        return cls._instance

    def __init__(self,
        url: str,
        timeout: int
    ):
        if getattr(self,'_initialized', False):
            return 
        self._initialize(url, timeout)

    def _initialize(self,
        url: str,
        timeout: int
    ):
        self._initialized = True
        self.session = requests.Session()
        self.timeout = timeout
        self.url = url

    def _build_url(self, path: str) -> str:
        return f"{self.url}/{path}"

    def request(self,
        method: str,
        endpoint: str,
        data: Optional[T] = None,
        params: Optional[Dict[str, Any]] = None
    ) -> requests.Response:
        url = self._build_url(endpoint)
        response = self.session.request(
            method,
            url,
            json=data,
            params=params,
            timeout=self.timeout
        )
        response.raise_for_status()
        return response

    def get(self,
        endpoint: str,
        params: Optional[Dict[str, Any]] = None
    ) -> R:
        res =  self.request('GET', endpoint, params=params)
        return res.json()

    def post(self,
        endpoint: str,
        data: T
    ) -> R:
        res = self.request('POST', endpoint, data)
        return res.json()


