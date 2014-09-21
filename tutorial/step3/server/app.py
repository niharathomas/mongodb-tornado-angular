"""
app.py
revision: 0.1 24.4.2014 initial by David Levy
Step:1
Tornado server for mongodb tornado angular
"""
import tornado
import os
from tornado import ioloop, web
class IndexHandler(web.RequestHandler):
    def get(self):
        self.render("../templates/index.html")

app = tornado.web.Application([
                          (r'/', IndexHandler),
                      ],
                      autoreload=True
)

if __name__ == '__main__':
    port = 9915
    print('server running on http://localhost:{}'.format(port))
    app.listen(port)
    ioloop = ioloop.IOLoop.instance()
    ioloop.start()
