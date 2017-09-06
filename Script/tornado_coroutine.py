import time
import tornado.ioloop
import tornado.web
import tornado.gen

class BadStupidHandler(tornado.web.RequestHandler):
    def get(self):
        for i in range(20):
            self.write('{}<br>'.format(i))
            self.flush()
            time.sleep(0.5)

class GoodStupidHandler(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def get(self):
        for i in range(20):
            self.write('{}<br>'.format(i))
            self.flush()
            yield time.sleep(0.5)


if __name__ == "__main__":
    app=tornado.web.Application([
        (r'/bad',BadStupidHandler),
        (r'/good', GoodStupidHandler)
    ])
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()