import tornado.ioloop
import tornado.web

def divide(a,b):
    if b == 0:
        return 'Нельзя делить на ноль'
    return a/b


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        a = int(self.get_argument('a'))
        b = int(self.get_argument('b'))

        self.write({'res': divide(a,b)})

main = tornado.web.Application({(r"/", MainHandler)})

main.listen(8000)
tornado.ioloop.IOLoop.current().start()
