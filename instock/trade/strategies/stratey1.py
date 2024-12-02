#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import time
from datetime import datetime

from ..robot.infrastructure.strategy_template import StrategyTemplate

class Strategy(StrategyTemplate):
    """Example strategy"""
    
    name = 'Example Strategy'
    
    def init(self):
        """Initialize strategy"""
        # Get timestamp through the following method
        self.start_time = time.time()
    
    def clock(self, event):
        """Clock event handler"""
        # Register clock event
        if event.data.clock_event == "1m":
            self.strategy()
        
        # Register clock interval event, will trigger even outside trading hours, clock_type == minute_interval
        elif event.data.clock_event == "5m":
            self.strategy()
    
    def strategy(self):
        """Strategy implementation"""
        # --------Write trading strategy---------
        print(f"Strategy running at {datetime.now()}")
        # --------Write trading strategy---------
