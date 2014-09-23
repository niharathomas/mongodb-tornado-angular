"""
app.py
revision: 0.1 24.4.2014 initial by David Levy

Tornado server for mongodb tornado angular tutorial
"""
import os
import sys
import tornado
import pymongo
from tornado.options import  options
from tornado import ioloop, web

#adding local directory to path
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

"""
Loading default setting files
"""
import settings

"""
searching for a local_setting.py file that overrides default configuration
"""
try:
    tornado.options.parse_config_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)),'local_settings.py'),
        False)
except Exception as e:
    #print ('local settings: {}'.format(str(e)))
    #TODO: handle different exceptions
    print ('local_settings.py not defined, using default settings')

"""
Connecting to the mongodb database
"""
mongo_client = pymongo.MongoClient(options.mongodb_host)
db = mongo_client[options.mongodb_name]


class IndexHandler(web.RequestHandler):
    def get(self):
        """
        Loading the main page for the application
        As we are working in a single web page application it might be the only page to load
        """
        self.render("../templates/index.html")

class ApiHandler(tornado.web.RequestHandler):
    def initialize(self, db):
        """
        Initializes the instance with a mongo database instance
        :param db: an instance to pymongo database object
        """
        self._db = db

    def get(self):
        self.render("../templates/index.html")
app = tornado.web.Application([
                          (r'/', IndexHandler),
                          (r'/api', ApiHandler, dict(db=db))
                      ],
                      static_path=os.path.join(os.path.dirname(__file__), '../client/'),
                      autoreload=True
)

if __name__ == '__main__':
    #read settings from commandline
    options.parse_command_line()
    print ('server running on http://localhost:{}'.format(options.port))
    app.listen(options.port,xheaders=True)
    ioloop = tornado.ioloop.IOLoop.instance()
    ioloop.start()
