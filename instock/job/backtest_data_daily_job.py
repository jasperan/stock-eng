#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import datetime
import pandas as pd
import numpy as np

from ..lib.database import engine, insert_db
from ..lib.run_template import get_run_date_list

def process_backtest_data(date_str):
    """Process stock strategy backtesting data"""
    
    # Get engine connection
    conn = engine.connect()
    
    # Backtesting table
    table_name = "stock_strategy_backtest"
    
    # Get strategy data
    sql = f"""
    SELECT code, name, strategy_name, strategy_type, buy_date, sell_date, 
           buy_price, sell_price, (sell_price - buy_price) / buy_price * 100 as profit_rate
    FROM stock_strategy 
    WHERE buy_date <= '{date_str}'
    """
    
    df = pd.read_sql(sql, conn)
    
    if df.empty:
        return
    
    # Calculate statistics
    stats = {
        "date": date_str,
        "total_trades": len(df),
        "profitable_trades": len(df[df["profit_rate"] > 0]),
        "avg_profit_rate": df["profit_rate"].mean(),
        "max_profit_rate": df["profit_rate"].max(),
        "min_profit_rate": df["profit_rate"].min(),
        "std_profit_rate": df["profit_rate"].std()
    }
    
    # Insert into database
    stats_df = pd.DataFrame([stats])
    insert_db(stats_df, table_name)

def main():
    """Main function entry"""
    date_list = get_run_date_list()
    for date_str in date_list:
        process_backtest_data(date_str)

if __name__ == "__main__":
    main()
