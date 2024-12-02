#!/usr/local/bin/python3
# -*- coding: utf-8 -*-


class singleton_type(type):
    """
    Singleton metaclass for implementing the singleton pattern.
    """
    
    def __init__(cls, name, bases, dict):
        super(singleton_type, cls).__init__(name, bases, dict)
        cls._instance = None
    
    def __call__(cls, *args, **kwargs):  # Called when creating an object of cls
        if cls._instance is None:
            cls._instance = super(singleton_type, cls).__call__(*args, **kwargs)  # Create cls object
        return cls._instance
