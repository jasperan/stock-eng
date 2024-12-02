#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import os.path
import sys
import torndb
import tornado.web
import tornado.ioloop
import tornado.options
import tornado.httpserver
import configparser
from tornado.options import define, options
from tornado.web import RequestHandler

# Temporarily add project path to environment variables during project runtime
cwd = os.getcwd()  # Get current working directory
sys.path.append(os.path.join(cwd, ".."))

from web.base import BaseHandler
from web.dataTableHandler import GetStockDataHandler
from web.dataIndicatorsHandler import GetDataIndicatorsHandler
from web.dataIndicatorsHandler import AddStockWatchHandler

# Set routes
handlers = [
    (r"/", BaseHandler),
    # Use datatable to display report data module
    (r"/stock/api_data", GetStockDataHandler),
    # Get stock indicator data
    (r"/stock/api_indicators", GetDataIndicatorsHandler),
    # Add to watchlist
    (r"/stock/api_watch", AddStockWatchHandler),
]

settings = dict(  # Configuration
    template_path=os.path.join(os.path.dirname(__file__), "templates"),
    static_path=os.path.join(os.path.dirname(__file__), "static"),
    debug=True,
    xsrf_cookies=False,
    # Cookie encryption
    cookie_secret="027bb1b3-f01c-47b7-b107-b52f56cef9ad",
)

# Main function entry
if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers, **settings)
    http_server = tornado.httpserver.HTTPServer(app)
    port = 9988
    http_server.listen(port)
    tornado.ioloop.IOLoop.current().start()
