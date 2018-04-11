import time

import tornado.gen
import tornado.ioloop
import tornado.web

lst = [
    ':7iir:&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspiriir,&nbsp&nbsp.&nbsp...&nbsp.....&nbsp...&nbsp.&nbsp.&nbsp.B@B@k&nbsp&nbsp&nbsp&nbsp@B@BM&nbsp&nbsp&nbsp...&nbsp...&nbsp.&nbsp.&nbsp.&nbsp.&nbsp',
    'OB@B@Z&nbsp&nbsp.&nbsp.&nbsp&nbspB@B@B5&nbsp&nbsp&nbsp.&nbsp.&nbsp.&nbsp.&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp.&nbsp.&nbsp&nbsp.@B@BO&nbsp&nbsp&nbsp&nbspB@B@B&nbsp&nbsp.&nbsp.&nbsp.&nbsp.&nbsp.&nbsp&nbsp&nbsp&nbsp&nbsp.&nbsp.',
    '5@B@BS&nbsp&nbsp&nbsp.&nbsp&nbsp&nbspMB@B@7&nbsp&nbsp.&nbsp.&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspB@B@q&nbsp&nbsp&nbsp&nbsp@B@BM&nbsp&nbsp..&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp.&nbsp',
    '1B@B@U&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspN@B@Bv&nbsp&nbsp&nbsp.&nbsp&nbsp&nbsp&nbsp&nbspi7vrr.&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp.@B@Bq&nbsp&nbsp&nbsp&nbspB@B@O&nbsp&nbsp.&nbsp&nbsp&nbsp&nbsp&nbsp:i777i,&nbsp&nbsp&nbsp',
    '2@B@Bv&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspS@@B@7&nbsp&nbsp.&nbsp&nbsp&nbspFB@B@B@B@Bq.&nbsp&nbsp&nbsp&nbsp.B@B@X&nbsp&nbsp&nbsp&nbsp@B@BM&nbsp&nbsp&nbsp&nbsp&nbsp:O@B@B@@@B@S.',
    '1@@B@Pr7LLJrvO@B@Bv&nbsp&nbsp&nbsp&nbspi@@@B@uvLOB@@@;&nbsp&nbsp&nbsp.@B@Bq&nbsp&nbsp&nbsp&nbspB@B@O&nbsp&nbsp&nbsp&nbspPB@@@B8FMB@B@B7',
    '2@B@@@B@B@@@B@B@B@r&nbsp&nbsp&nbsp.@B@@S&nbsp&nbsp&nbsp&nbsp&nbspvB@B@.&nbsp&nbsp.B@B@P&nbsp&nbsp&nbsp&nbsp@B@BM&nbsp&nbsp&nbspJB@B@N&nbsp&nbsp&nbsp&nbsp.B@B@B:',
    '5B@B@B@B@B@BBB@B@B7&nbsp&nbsp&nbspuB@B@MBB@BBM@B@Bq&nbsp&nbsp.@B@Bq&nbsp&nbsp&nbsp&nbspB@@@M&nbsp&nbsp&nbspM@B@@.&nbsp&nbsp&nbsp&nbsp&nbsp7B@B@u',
    '2@B@BY&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspXB@B@7&nbsp&nbsp&nbspF@@@B@B@B@B@B@B@S&nbsp&nbsp.B@B@P&nbsp&nbsp&nbsp&nbsp@B@BM&nbsp&nbsp&nbsp@B@B@&nbsp&nbsp&nbsp&nbsp&nbsp&nbspi@B@B2',
    '2B@B@j&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspP@B@Bv&nbsp&nbsp&nbsp;B@B@r&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp@B@@P&nbsp&nbsp&nbsp&nbspB@B@O&nbsp&nbsp&nbspX@B@@7&nbsp&nbsp&nbsp&nbsp&nbspqB@@@r',
    '5@B@@5&nbsp&nbsp&nbsp.&nbsp&nbsp&nbsp8B@B@7&nbsp&nbsp&nbsp&nbspGB@B@J.&nbsp&nbsp&nbsp&nbsp:LO@&nbsp&nbsp&nbsp.B@B@P&nbsp&nbsp&nbsp&nbsp@B@BM&nbsp&nbsp&nbsp,B@B@@1:.:GB@@@O&nbsp',
    'qB@B@X&nbsp&nbsp&nbsp&nbsp.&nbsp&nbspB@B@BJ&nbsp&nbsp&nbsp&nbsp&nbspjB@B@B@B@B@B@@&nbsp&nbsp&nbsp.@B@BO&nbsp&nbsp&nbsp&nbspB@B@B&nbsp&nbsp&nbsp&nbsp.E@B@@@@@B@B@F&nbsp',
    '2@B@@2&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp0B@@@7&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp:UO@B@@@qui,&nbsp&nbsp&nbsp,B@B@k&nbsp&nbsp&nbsp.B@@BM.&nbsp&nbsp&nbsp&nbsp&nbsp.7S@B@BM5r&nbsp']


class BadStupidHandler(tornado.web.RequestHandler):
    def get(self):
        for line in lst:
            self.write('{}<br>'.format(line))
            self.flush()
            time.sleep(0.5)


class GoodStupidHandler(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def get(self):
        for line in lst:
            self.write('{}<br>'.format(line))
            self.flush()
            yield tornado.gen.sleep(0.5)


if __name__ == "__main__":
    app = tornado.web.Application([
        (r'/bad', BadStupidHandler),
        (r'/good', GoodStupidHandler)
    ])
    app.listen(8001)
    tornado.ioloop.IOLoop.current().start()
