#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import os
import pymysql
from sqlalchemy import create_engine
from sqlalchemy.types import NVARCHAR
from sqlalchemy import inspect

__author__ = 'myh '
__date__ = '2023/3/10 '

db_host = "localhost"  # Database server host
db_user = "root"  # Database access user
db_password = "root"  # Database access password
db_database = "instockdb"  # Database name
db_port = 3306  # Database service port
db_charset = "utf8mb4"  # Database character set

# Get database configuration from environment variables, passed through docker -e
db_host = os.environ.get('db_host') if os.environ.get('db_host') else db_host
db_user = os.environ.get('db_user') if os.environ.get('db_user') else db_user
db_password = os.environ.get('db_password') if os.environ.get('db_password') else db_password
db_database = os.environ.get('db_database') if os.environ.get('db_database') else db_database
db_port = os.environ.get('db_port') if os.environ.get('db_port') else db_port
db_charset = os.environ.get('db_charset') if os.environ.get('db_charset') else db_charset

# Create the database connection string
DB_CONN_URL = f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_database}?charset={db_charset}"

# Database connection engine
engine = create_engine(
    DB_CONN_URL,
    encoding='utf8',
    echo=False,
    max_overflow=0,  # Maximum number of connections to overflow
    pool_size=5,  # Connection pool size
    pool_timeout=30,  # Connection pool timeout
    pool_recycle=1*3600  # Connection pool recycle time
)

# DB Api - Database connection object
conn = engine.connect()

def insert_db(data, table_name, write_index=False, primary_keys=None):
    """
    Define a general method function to insert data into database tables and create database primary keys,
    ensuring index uniqueness when rerunning data.
    """
    # Insert into default database
    return _insert_impl(data, table_name, write_index, primary_keys, DB_CONN_URL)

def insert_other_db(data, table_name, write_index, primary_keys, url):
    """Add a method to insert into other databases."""
    return _insert_impl(data, table_name, write_index, primary_keys, url)

def _insert_impl(data, table_name, write_index, primary_keys, url):
    # Define engine
    engine = create_engine(
        url,
        encoding='utf8',
        echo=False
    )
    # Using http://docs.sqlalchemy.org/en/latest/core/reflection.html
    # Use inspection to check if the database table has a primary key
    insp = inspect(engine)
    if primary_keys is None:
        # If there is an index, add the index to varchar
        data.to_sql(table_name, engine, index=write_index, if_exists='append')
    else:
        # Insert at the first position:
        dtype = {}
        for k in primary_keys:
            dtype[k] = NVARCHAR(40)
        data.to_sql(table_name, engine, index=write_index, if_exists='append', dtype=dtype)
        # Check if primary key exists
        if not insp.get_pk_constraint(table_name)['constrained_columns']:
            with engine.connect() as con:
                # Execute database insert data
                con.execute('ALTER TABLE `%s` ADD PRIMARY KEY (%s);' % (table_name, ",".join(primary_keys)))
    return True

def update_data(sql):
    """Update data"""
    try:
        conn.execute(sql)
    except Exception as e:
        print("Execution error: " + sql)
        print(e)

def query_data(sql):
    """Query data"""
    result = []
    try:
        result = conn.execute(sql).fetchall()
    except Exception as e:
        print("Execution error: " + sql)
        print(e)
    return result

def check_table_exists(table_name):
    """Check if table exists"""
    return inspect(engine).has_table(table_name)

def execute(sql, params=None):
    """Execute SQL"""
    try:
        if params is None:
            conn.execute(sql)
        else:
            conn.execute(sql, params)
    except Exception as e:
        print("Execution error: " + sql)
        print(e)

def query(sql, params=None):
    """Query data"""
    result = []
    try:
        if params is None:
            result = conn.execute(sql).fetchall()
        else:
            result = conn.execute(sql, params).fetchall()
    except Exception as e:
        print("Execution error: " + sql)
        print(e)
    return result

def count(sql, params=None):
    """Count records"""
    result = []
    try:
        if params is None:
            result = conn.execute(sql).fetchall()
        else:
            result = conn.execute(sql, params).fetchall()
    except Exception as e:
        print("Execution error: " + sql)
        print(e)
    return int(result[0][0])
