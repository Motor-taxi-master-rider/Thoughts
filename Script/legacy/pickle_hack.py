import pickle


class A(object):
    def __init__(self, a):
        self.val = a

    def __getattr__(self, item):
        print(item)
        if item == '__getnewargs__':
            return lambda: (self.__class__, self.val)
        if item == '__getstate__':
            return lambda: self.__dict__
        if item == '__setstate__':
            def _getstate(state):
                self.__dict__ = state

            return _getstate
        return str


class B(object):
    def __init__(self):
        self.c = A('a')


print(pickle.HIGHEST_PROTOCOL)
asd = B()
print(asd.c.__dict__)
print(asd.c.val)
asd.c.__getstate__()
a = pickle.dumps(B(), protocol=pickle.HIGHEST_PROTOCOL)
b = pickle.loads(a)
print(b.c.val)
