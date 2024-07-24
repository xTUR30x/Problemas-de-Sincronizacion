import logging
import os

class Logger:
    _instance = None

    def __new__(cls, filename, level):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance.logfile = filename
            cls._instance.level = level
            cls._instance.initialize()
        return cls._instance

    def initialize(self):
        if self.level == 'info':
            logging.basicConfig(filename=self.logfile, level=logging.INFO)
        self.create_logfile()


    def create_logfile(self):
        if not os.path.isfile(self.logfile):
            with open(self.logfile, "w") as archivo:
                print("Archivo creado")

    def log_message(self, message, level):
        levels = {
            'DEBUG': logging.DEBUG,
            'INFO': logging.INFO,
            'WARNING': logging.WARNING,
            'ERROR': logging.ERROR,
            'CRITICAL': logging.CRITICAL
        }

        if level in levels:
            logger = logging.getLogger()
            logger.log(levels[level], message)
        else:
            print(f"Nivel de log '{level}' no válido.")