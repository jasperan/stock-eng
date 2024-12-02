#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import os.path
import sys

# Temporarily add project path to environment variables during project runtime
cwd = os.getcwd()  # Get current working directory
sys.path.append(os.path.join(cwd, ".."))

from trade.robot.engine.main_engine import MainEngine
from trade.robot.engine.event_engine import EventEngine
from trade.robot.infrastructure.log import logger

def main():
    """Main function entry"""
    event_engine = EventEngine()
    main_engine = MainEngine(event_engine)
    
    # Strategy file will be automatically reloaded when modified, not recommended for production environment
    main_engine.is_watch_strategy = True
    
    main_engine.load_strategy()
    main_engine.start()

if __name__ == "__main__":
    main()
