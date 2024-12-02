#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod
from typing import Optional

from ..infrastructure.log import logger

class StrategyTemplate(ABC):
    """Base class for all strategies"""

    def __init__(self, log_handler=None):
        """Initialize strategy"""
        # Prioritize using custom log handler, otherwise use main engine log handler
        self.log = log_handler if log_handler else logger
        
        # Perform relevant initialization operations
        self.init()
    
    def init(self):
        """Initialize strategy, can be overridden by child classes"""
        pass
    
    @abstractmethod
    def clock(self, event):
        """Clock event handler, must be implemented by child classes"""
        pass
    
    def shutdown(self):
        """Shutdown strategy, can be overridden by child classes"""
        pass
