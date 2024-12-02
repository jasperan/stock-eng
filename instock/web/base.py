#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import os.path
import tornado.web
import configparser
from abc import ABC

# Base handler, mainly responsible for checking MySQL database connection
class BaseHandler(tornado.web.RequestHandler, ABC):
    @property
    def db(self):
        return self.application.db

    def get(self):
        self.render("index.html", leftMenu=GetLeftMenu(self.request.uri))

# Get left menu
def GetLeftMenu(uri):
    config = configparser.ConfigParser()
    config_path = os.path.join(os.path.dirname(__file__), "config.ini")
    config.read(config_path)
    menu_data = config.items("menu")
    menu_list = []
    for menu_item in menu_data:
        menu_list.append({"url": menu_item[1], "name": menu_item[0], "active": "active" if uri == menu_item[1] else ""})
    return menu_list
