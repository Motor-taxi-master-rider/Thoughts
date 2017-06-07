class Singleton(type):
    def __new__(cls, name, base, dct):
        dct['_instance'] = None
        return super().__new__(cls, name, base, dct)

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class Spam(metaclass=Singleton):
    def __init__(self):
        print('Creating Spam')


a = Spam()
b = Spam()
print(a is b)

c = Spam()
print(a is c)
