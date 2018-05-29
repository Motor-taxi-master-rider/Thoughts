import logging

DEFAULT_FORMAT = {'fmt': '[%(levelname)s %(asctime)s] \033[1;32;40m%(name)s\033[0m: %(message)s',
                  'datefmt': "%H:%M:%S"}


class MyLogger(logging.Logger):
    def __init__(self, name):
        super().__init__(name)
        self.set()

    def set(self):
        self.setLevel(logging.DEBUG)

        formatter = logging.Formatter(**DEFAULT_FORMAT)
        ch = logging.StreamHandler()
        ch.setFormatter(formatter)
        self.addHandler(ch)
