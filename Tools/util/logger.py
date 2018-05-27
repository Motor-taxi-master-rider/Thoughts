import logging


class MyLogger(logging.Logger):
    def __init__(self, name):
        super().__init__(name)
        self.set()

    def set(self):
        self.setLevel(logging.DEBUG)

        formatter = logging.Formatter('[%(levelname)s %(asctime)s]%(name)s: %(message)s',"%H:%M:%S")
        ch = logging.StreamHandler()
        ch.setFormatter(formatter)
        self.addHandler(ch)
