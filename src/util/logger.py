#!/usr/bin/env python3.12

import logging

fmt = "[%(levelname)s] %(asctime)s %(name)s: %(message)s"

class Logger:
    logger: logging.Logger

    def __init__(
        self,
        name: str,
        level: str
    ) -> None:

        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        self.logger.propagate = False

        handler = logging.StreamHandler()
        handler.setLevel(level)
        handler.setFormatter(logging.Formatter(fmt))
        self.logger.addHandler(handler)

    def info(self, message: str):
        self.logger.info(message)

    def exception(self, message: str):
        self.logger.exception(message)

    def warning(self, message: str):
        self.logger.warning(message)
    
    def debug(self, message: str):
        self.logger.debug(message)

    def critical(self, message: str):
        self.logger.critical(message)

