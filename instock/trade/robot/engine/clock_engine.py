#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import time
import datetime
from typing import Dict, List, Optional
from dateutil import tz

from ..infrastructure.log import logger
from .event_engine import EventEngine

class ClockEngine:
    """Clock engine for managing time-based events"""
    
    def __init__(self, event_engine: EventEngine, timezone: Optional[datetime.tzinfo] = None):
        """Initialize clock engine"""
        self.event_engine = event_engine
        self.is_active = True
        
        # Default to local timezone
        self.timezone = timezone or tz.tzlocal()
        
        # Event handlers
        self.clock_engine_handlers = []
        
        # Market open/close times
        self.trading_state = True
        self.clock_moment_handlers = {
            "open": (datetime.time(9, 30, 0), self._open_handler),
            "lunch_break": (datetime.time(11, 30, 0), self._lunch_break_handler),
            "afternoon_open": (datetime.time(13, 0, 0), self._afternoon_open_handler),
            "close": (datetime.time(15, 0, 0), self._close_handler),
        }
        
        # Interval events
        self.clock_interval_handlers = []
    
    def _is_trading_date(self, now: datetime.datetime) -> bool:
        """Check if it's a trading day"""
        # Only trigger on trading days
        if now.weekday() >= 5:
            return False
        return True
    
    def _open_handler(self, event):
        """Market open event handler"""
        self.trading_state = True
        logger.info("Market opened")
    
    def _lunch_break_handler(self, event):
        """Lunch break event handler"""
        self.trading_state = False
        logger.info("Lunch break started")
    
    def _afternoon_open_handler(self, event):
        """Afternoon open event handler"""
        self.trading_state = True
        logger.info("Afternoon session opened")
    
    def _close_handler(self, event):
        """Market close event handler"""
        self.trading_state = False
        logger.info("Market closed")
    
    def register_moment(self, clock_type: str, moment: datetime.time):
        """Register moment event"""
        self.clock_moment_handlers[clock_type] = (moment, None)
    
    def register_interval(self, interval: float, trading: bool = True):
        """Register interval event"""
        self.clock_interval_handlers.append((interval, trading))
    
    def start(self):
        """Start clock engine"""
        self.is_active = True
        
        while self.is_active:
            now = datetime.datetime.now(self.timezone)
            
            if not self._is_trading_date(now):
                time.sleep(1)
                continue  # Pause clock engine on holidays
            
            # Interval events
            for interval, trading_only in self.clock_interval_handlers:
                if not trading_only or self.trading_state:
                    self._check_interval_event(now, interval)
            
            # Moment events
            for clock_type, (moment, handler) in self.clock_moment_handlers.items():
                if now.time() >= moment:
                    if handler:
                        handler(None)
                    self.clock_moment_handlers[clock_type] = (moment, None)
            
            # Re-sort triggered events
            self.clock_moment_handlers = dict(sorted(
                self.clock_moment_handlers.items(),
                key=lambda x: x[1][0]
            ))
            
            time.sleep(1)
    
    def stop(self):
        """Stop clock engine"""
        self.is_active = False
