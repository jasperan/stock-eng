#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import json
import datetime
from abc import ABC
import tornado.web
import tornado.escape
from tornado import gen

from .base import BaseHandler

class GetStockDataHandler(BaseHandler, ABC):
    """Handler for getting stock data"""
    
    @gen.coroutine
    def get(self):
        """Get page data"""
        draw = self.get_argument("draw", "1")
        start = self.get_argument("start", "0")
        length = self.get_argument("length", "10")
        search = self.get_argument("search[value]", "")
        order_column = self.get_argument("order[0][column]", "0")
        order_dir = self.get_argument("order[0][dir]", "desc")
        
        sql = self.get_argument("sql", "")
        print("Executing SQL:", sql)
        
        # Get stock data content
        stock_web_list = self.db.query(sql)
        
        # Format response
        response = {
            "draw": draw,
            "recordsTotal": len(stock_web_list),
            "recordsFiltered": len(stock_web_list),
            "data": []
        }
        
        for stock in stock_web_list:
            response["data"].append(list(stock.values()))
        
        self.write(json.dumps(response, default=str))
