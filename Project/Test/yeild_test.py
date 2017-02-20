def coroutine():
    for i in range(1, 10):
        print("From generator")
        print("From generator {}".format((yield i)))
c = coroutine()
print(c.send(None))
print(list(x for x in range(1,10)))
try:
    while True:
        print("From user")
        print("From user {}".format(c.send(1)))
except StopIteration: pass
