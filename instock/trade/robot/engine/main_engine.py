#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import os
import sys
import time
import signal
import threading
from collections import defaultdict
from importlib import import_module
from types import ModuleType
from typing import Dict, List, Tuple

from ..infrastructure.log import logger
from ..infrastructure.strategy_wrapper import StrategyWrapper
from .event_engine import EventEngine

class MainEngine:
    """Main engine for managing strategies and events"""
    
    def __init__(self, event_engine: EventEngine):
        """Initialize main engine"""
        self.event_engine = event_engine
        
        # Login account
        self.account = None
        
        # Strategy instances
        self.strategies = {}
        
        # Strategy wrappers
        self.strategy_wrappers = {}
        
        # Save loaded strategy classes
        self.strategy_classes = {}
        
        # Whether to dynamically reload strategies
        self.is_watch_strategy = False
        
        # Modified time cache
        self.strategy_file_mt_map = {}
        
        # File process mapping
        self.strategy_process_map = {}
        
        # File module mapping
        self.strategy_module_map = {}
        
        # Loading lock
        self._strategy_lock = threading.Lock()
        
        # Loading thread
        self._strategy_thread = None
        
        # Shutdown functions
        self.before_shutdown = []  # Functions to execute before engine shutdown
        self.main_shutdown = []  # Functions for engine's own shutdown
        self.after_shutdown = []  # Functions to execute after engine shutdown
        
        signal.signal(
            signal.SIGINT,  # Keyboard signal
            self._shutdown
        )
        signal.signal(
            signal.SIGTERM,  # Kill command
            self._shutdown
        )
    
    def _shutdown(self, sig, frame):
        """Single shutdown interface to be called after capturing exit signals"""
        logger.info("Received exit signal, executing shutdown sequence...")
        
        for func in self.before_shutdown:
            logger.debug("Executing pre-shutdown function: %s", func.__name__)
            func()
        
        self.stop()
        
        for func in self.after_shutdown:
            logger.debug("Executing post-shutdown function: %s", func.__name__)
            func()
        
        logger.info("Shutdown sequence completed")
        sys.exit(0)
    
    def load_strategy(self):
        """Load strategy"""
        with self._strategy_lock:
            self._load_strategy()
    
    def _load_strategy(self):
        """Internal method to load strategy"""
        # Check if need to reload
        for strategy_file, strategy_module in self.strategy_module_map.items():
            # Get module instance from cache
            new_module = self._load_strategy_module(
                strategy_file,  # Get module instance from cache
                import_module(strategy_module.__name__)  # Create new module instance
            )
            
            if new_module is None:
                continue
                
            # Check last modified time
            file_mt = os.stat(strategy_file).st_mtime
            if file_mt > self.strategy_file_mt_map[strategy_file]:
                # Unregister strategy's listeners
                for strategy_name in self.strategy_process_map[strategy_file]:
                    self.strategy_wrappers[strategy_name].stop()
                    self.strategies.pop(strategy_name, None)
                
                # Reload
                self.strategy_module_map[strategy_file] = new_module
                self.strategy_file_mt_map[strategy_file] = file_mt
                
                # Cache loading info
                for name, strategy_class in new_module.__dict__.items():
                    if getattr(strategy_class, 'is_strategy', False):
                        self.strategy_classes[name] = strategy_class
                        strategy = strategy_class(self)
                        self.strategies[name] = strategy
                        self.strategy_wrappers[name] = StrategyWrapper(strategy)
                        self.strategy_process_map[strategy_file].append(name)
    
    def start(self):
        """Start engine"""
        # Clock event
        self.event_engine.start()
        
        # Start strategy wrappers
        for strategy_wrapper in self.strategy_wrappers.values():
            strategy_wrapper.start()
        
        # If thread hasn't started, start strategy monitoring thread
        if self.is_watch_strategy and self._strategy_thread is None:
            self._strategy_thread = threading.Thread(target=self._watch_strategy)
            self._strategy_thread.daemon = True
            self._strategy_thread.start()
    
    def stop(self):
        """Stop engine"""
        # All pre-shutdown triggers
        for func in self.before_shutdown:
            func()
        
        # Engine's own shutdown
        self.event_engine.stop()
        
        # Wait for all threads to close until only main thread remains
        for strategy_wrapper in self.strategy_wrappers.values():
            strategy_wrapper.stop()
        
        # Call strategy's shutdown
        for strategy in self.strategies.values():
            if hasattr(strategy, 'shutdown'):
                strategy.shutdown()
        
        # All post-shutdown triggers
        for func in self.after_shutdown:
            func()
        
        # Exit
        sys.exit(0)
    
    def _watch_strategy(self):
        """Watch strategy files for changes"""
        while True:
            try:
                self.load_strategy()
            except Exception as e:
                logger.error("Strategy reload failed: %s", e)
            time.sleep(2)
