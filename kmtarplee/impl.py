'''implementation of something'''
import math

import tornado.ioloop
import tornado.web

def f(x, y, z):
    '''adds numbers'''
    return x + y + z

def h(x):
    '''computes the sine of x'''
    return math.sin(x)

#Tornado code

class MainHandler(tornado.web.RequestHandler):
    '''Some handler class'''
    def get(self):
        '''handle HTTP GET request'''
        self.write("Hello, world")

def server_listen(port=8888):
    '''tries to use tornado'''
    application = tornado.web.Application([
        (r"/", MainHandler),
    ])

    application.listen(port)
    tornado.ioloop.IOLoop.current().start()
