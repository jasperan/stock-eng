#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import queue
import threading
from collections import defaultdict
from typing import Dict, List, Callable

from ..infrastructure.log import logger

class EventEngine:
    """Event Engine for handling and distributing events"""
    
    def __init__(self):
        """Initialize event engine"""
        
        # Event queue
        self._queue = queue.Queue()
        
        # Event engine switch
        self._active = False
        
        # Event engine processing thread
        self._thread = threading.Thread(target=self._run)
        
        # Event dictionary, key is event type, value is list of corresponding event handler functions
        self._handlers: Dict[str, List[Callable]] = defaultdict(list)
    
    def _run(self):
        """Run event engine"""
        while self._active:
            try:
                event = self._queue.get(block=True, timeout=1)
                self._process(event)
            except queue.Empty:
                pass
    
    def _process(self, event):
        """Process events"""
        # Check if there are corresponding handler functions for this event
        if event.type_ in self._handlers:
            # If exists, pass the event to handler functions in sequence
            [handler(event) for handler in self._handlers[event.type_]]
    
    def start(self):
        """Start event engine"""
        self._active = True
        self._thread.start()
    
    def stop(self):
        """Stop event engine"""
        self._active = False
        self._thread.join()
    
    def register(self, type_: str, handler: Callable):
        """Register event handler"""
        handler_list = self._handlers[type_]
        if handler not in handler_list:
            handler_list.append(handler)
    
    def unregister(self, type_: str, handler: Callable):
        """Unregister event handler"""
        handler_list = self._handlers[type_]
        if handler in handler_list:
            handler_list.remove(handler)
        if not handler_list:
            self._handlers.pop(type_)
    
    def put(self, event):
        """Put event into queue"""
        self._queue.put(event)
