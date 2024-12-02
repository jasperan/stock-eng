#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import json
from abc import ABC
import tornado.web
import tornado.escape
from tornado import gen

from .base import BaseHandler

class GetDataIndicatorsHandler(BaseHandler, ABC):
    """Handler for getting stock indicators data"""
    
    @gen.coroutine
    def get(self):
        """Get page data"""
        code = self.get_argument("code", "")
        sql = f"SELECT * FROM stock_indicators WHERE code = '{code}' ORDER BY date DESC LIMIT 1"
        stock_indicators = self.db.query(sql)
        
        response = {
            "success": True,
            "data": stock_indicators[0] if stock_indicators else None
        }
        
        self.write(json.dumps(response, default=str))

class AddStockWatchHandler(BaseHandler, ABC):
    """Handler for adding stocks to watchlist"""
    
    @gen.coroutine
    def get(self):
        """Add stock to watchlist"""
        code = self.get_argument("code", "")
        sql = f"INSERT INTO stock_watch (code) VALUES ('{code}')"
        self.db.execute(sql)
        
        response = {
            "success": True,
            "message": f"Added {code} to watchlist"
        }
        
        self.write(json.dumps(response))