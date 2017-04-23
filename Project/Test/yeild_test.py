class Enum(tuple): __getattr__ = tuple.index

BrowserType = Enum(['FIREFOX', 'CHROME', 'IE', 'SAFARI', 'PHANTOMJS'])
print(State.Claimed)
