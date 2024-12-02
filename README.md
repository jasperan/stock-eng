**InStock Stock System**

InStock is a stock analysis system that captures daily stock and ETF key data, calculates various stock indicators, identifies candlestick patterns, provides comprehensive stock screening, includes multiple stock selection strategies, supports backtesting verification, enables automated trading, supports batch processing, runs efficiently, and is compatible with PC, tablet, and mobile devices. It also provides a Docker image for easy installation, making it an excellent tool for quantitative investment.

Project Repository: https://github.com/myhhub/stock

Docker Image: https://hub.docker.com/r/mayanghua/instock **Optimized image size of only 170M**.

# Features

## I. Comprehensive Stock Screening
The comprehensive stock screening supports over 200 information columns for free combination screening across stock scope, fundamentals, technical indicators, news, popularity indicators, and market data. The screening conditions are categorized as follows:

```
1. Stock Scope
Market, Industry, Region, Concept, Style, Index Components, Listing Time.
2. Fundamentals
Valuation indicators, Per Share indicators, Profitability, Growth capability, Capital structure and Solvency, Share capital and shareholders.
3. Technical Indicators
MACD Golden Cross, KDJ Golden Cross, Volume Breakout, Low-level Fund Inflow, High-level Fund Outflow, Upward Break through Moving Average, Bullish MA Alignment, Bearish MA Alignment, Continuous Rise with Volume, Decline with Low Volume, Single Large Yang Line, Double Large Yang Lines, Rising Sun, Strong Bulls, Cannon Through Clouds, Seven Fairies Descending (Seven Consecutive Negative), Eight Immortals Crossing Sea (Eight Consecutive Positive), Nine Yang Power (Nine Consecutive Positive), Four Consecutive Yang, Volume Rule, Volume Attack, Piercing Pattern, Inverted Hammer, Shooting Star, Evening Star, Dawn Break, Pregnant Pattern, Dark Cloud Cover, Morning Star, Narrow Range Consolidation.
4. News Aspects
Announcements and Events, Institutional Focus, Number of Institutional Shareholders, Institutional Shareholding Ratio.
5. Popularity Indicators
Stock Forum Popularity Ranking, Popularity Ranking Changes, Continuous Rise in Popularity Ranking, Continuous Drop in Popularity Ranking, New High in Popularity Ranking, New Low in Popularity Ranking, New Fans Ratio, Core Fans Ratio, 7-day Attention Ranking, Today's View Ranking.
6. Market Data
Stock Price Performance, Trading Information, Fund Flow, Market Statistics, Shanghai-Shenzhen Stock Connect.
```
![](img/a3.jpg)
![](img/a2.jpg)
![](img/a1.jpg)

## II. Daily Stock Data

Includes daily stock data, stock fund flows, stock dividends and distributions, stock dragon-tiger lists, stock block trades, stock fundamental data, industry fund flows, concept fund flows, and daily ETF data.

The system captures key A-share daily data and encapsulates data collection methods, making it easy to extend the system to obtain personally focused data.

![](img/00.jpg)
![](img/12.jpg)

## III. Stock Indicator Calculations
Based on talib and pandas for efficient and accurate indicator calculations. Some indicator formulas have been adjusted to ensure results match those from platforms like Tonghuashun and Tongxinda.
Indicators:

```
1. MACD 2. KDJ 3. BOLL 4. TRIX, TRMA 5. CR 6. SMA 7. RSI 
8. VR, MAVR 9. ROC 10. DMI, +DI, -DI, DX, ADX, ADXR 11. W&R 
12. CCI 13. TR, ATR 14. DMA, AMA 15. OBV 16. SAR 17. PSY 
18. BRAR 19. EMV 20. BIAS 21. TEMA  22. MFI 23. VWMA
24. PPO 25. WT 26. Supertrend  27. DPO  28. VHF  29. RVI
30. FI 31. ENE 32. STOCHRSI
```

![](img/01.jpg)
![](img/06.jpg)
![](img/13.jpg)
![](img/10.jpg)
![](img/02.jpg)

## IV. Stock Buy/Sell Signal Detection

Determines potential buy and sell signals based on indicators. The specific screening conditions are as follows:

```
KDJ:
1. Overbought Zone: When K value is above 80, D value above 70, and J value above 90, it's considered overbought. Generally, stock prices may decline. Investors should be cautious, outsiders should not chase higher prices, and insiders should consider selling.
2. Oversold Zone: When K value is below 20 and D value below 30, it's considered oversold. Generally, stock prices may rise with increased possibility of a rebound. Insiders should not hastily sell stocks, and outsiders may look for entry opportunities.

RSI:
1. When the 6-day indicator rises to 80, it indicates market overbought conditions. If it continues to rise above 90, it indicates a severe overbought warning zone, suggesting price tops may have formed with high possibility of short-term reversal.
2. When the 6-day RSI falls to 20, it indicates market oversold conditions. If it continues to fall below 10, it indicates a severe oversold zone, suggesting high possibility of price bottoming and reversal.

CCI:
1. When CCI > +100, it indicates prices have entered an abnormal zone - overbought zone, and price anomalies should be closely monitored.
2. When CCI < -100, it indicates prices have entered another abnormal zone - oversold zone, investors may consider accumulating stocks at low prices.

CR:
1. When price breaks below lines a, b, c, d and then climbs up 160 points from the low, it's a good opportunity for short-term profit-taking, and stocks should be sold appropriately.
2. When CR falls below 40, it's a good opportunity for building positions.

WR:
1. When %R reaches 20, the market is in an overbought condition, and trend may be reaching a top.
2. When %R reaches 80, the market is in an oversold condition, and stock prices may be bottoming at any time.

VR:
1. Profit-taking zone 160-450, take profits according to conditions.
2. Low-price zone 40-70 suitable for buying.
```

![](img/05.jpg)

## V. K-line Pattern Recognition

Accurately recognizes 61 types of K-line patterns, supporting user-selected pattern recognition.

Pattern recognition:

```
1. Two Crows 2. Three Crows 3. Three Internal Ups and Downs 4. Three Line Strike 5. Three External Ups and Downs 6. Southern Three Stars 7. Three White Soldiers 8. Abandoned Baby 9. Big Enemy Current 10. Catching the Belt 11. Breakout 12. Closing Line with No Shadow 13. Hidden Baby Swallowing 14. Counterattack Line 15. Overhead Press 16. Cross 17. Cross Star 18. Dragon Cross/T-Cross 19. Swallow Mode 20. Evening Star 21. Morning Star 22. Up/Down Jump Overlapping Rises 23. Grave Cross/Reverse T-Cross 24. Hammer 25. Hanging Man 26. Mother-Child Line 27. Cross Pregnant Line 28. Windy Line 29. Trap 30. Correction Trap 31. Dove 32. Triple Black Crows 33. Neck Line 34. Inverted Hammer 35. Reversal Pattern 36. Reversal Pattern with Long Shadow 37. Ladder Bottom 38. Long Leg Cross 39. Long Candle 40. Head and Tail/No Shadow 41. Same Low Price 42. Padding 43. Cross Morning Star 44. Morning Star 45. Neck Line 46. Penetration Pattern 47. Yellow Cab Driver 48. Three Methods 49. Separating Line 50. Shooting Star 51. Short Candle 52. Cone 53. Pause Pattern 54. Three-Line Sausage 55. Probe 56. Up/Down Jump Overlapping Rises 57. Insert 58. Three Stars 59. Unique Three Riverbed 60. Up/Down Jump Overlapping Rises 61. Up/Down Jump Overlapping Rises
```

Pattern recognition result:
```
Negative: Sell signal
0: No pattern
Positive: Buy signal
```
![](img/09.jpg)

![](img/06.jpg)

## VI. Stock Selection Strategies

Built-in放量上涨、停机坪、回踩年线、突破平台、放量跌停等多种选股策略，同时封装了策略模板，方便扩展实现自己的策略。


```
1. Volume Increase
    1) The increase on the day is less than 2% or the closing price is less than the opening price.
    2) The daily trading volume is not less than 200 million.
    3) The daily trading volume / 5-day average trading volume >= 2.
2. MA Bullish
    MA30 upward
    1) 30-day MA of 30 days ago < 20-day MA of 30 days ago < 10-day MA of 30 days ago < the 30-day MA of the current day.
    2) (The 30-day MA of the current day / 30-day MA of 30 days ago) > 1.2.
3. Stop and Go
    1) The last 15 days have a gain of more than 9.5%, and it must be a volume increase.
    2) The next trading day must open higher, close higher, and not be more than 3% away from the opening price.
    3) The next 2-3 trading days must open higher, close higher, and not be more than 3% away from the opening price, and the daily change must be within 5%.
4. Back to the 250-day line
    1) Divide into 2 periods: the first period is the last 60 trading days before the highest closing price (length > 0), and the second period is the trading days after the highest price.
    2) The first period must break through the 250-day line.
    3) The second period must be above the 250-day line, and the lowest price day and the highest price day must be within 10-50 days.
    4) Back to the 250-day line accompanied by a decrease in volume: the highest price day trading volume / the lowest price day trading volume > 2, the lowest price / the highest price < 0.8.
5. Breakout Platform
    1) The closing price of a stock on the 60th day is greater than or equal to the 60-day moving average > the opening price.
    2) And [1] volume increase.
    3) And [1] before this time, the closing price of any day is within -5% to 20% of the 60-day moving average.
6. No significant pullback
    1) The daily closing price is less than 0.6 times the closing price 60 days ago.
    2) In the past 60 days, there must not be a single day with a loss of more than 7%, a high opening low closing of 7%, two days of cumulative loss of 10%, or two days of high opening low closing of 10%.
7. Turtle Trading Rules
    The closing price of the last trading day is the highest price in the specified range.
    1) The closing price of the last trading day >= the highest closing price of the past 60 days.
8. High and Narrow Flag
    1) Must be traded for at least 60 days.
    2) The closing price / the lowest price of the past 24-10 days >= 1.9.
    3) The past 24-10 days must have two consecutive days of gains of at least 9.5%.
9. Volume跌停。
    1) The decline is more than 9.5%.
    2) The trading volume is not less than 200 million.
    3) The trading volume is at least 4 times the average trading volume of the past 5 days.
10. Low ATR Growth
    1) Must be traded for at least 250 days.
    2) The highest closing price of the past 10 days must be 1.1 times higher than the lowest closing price of the past 10 days.
11. Stock Fundamental Selection
    1) The price-earnings ratio is less than or equal to 20 and greater than 0.
    2) The price-to-book ratio is less than or equal to 10.
    3) The net asset return rate is greater than or equal to 15.
```

![](img/04.jpg)

## VII. Stock Selection Verification


对指标、策略等选出的股票进行回测，验证策略的成功率，是否可用。


![](img/05.jpg)

## VIII. Automated Trading

Supports automated trading, including automated新股策略及示例策略，由于**涉及金钱**，规避可能存在风险，没有提供其他交易策略。

Has trading logs and supports configuring trading logs for each trading strategy.

**Special Reminder**: The IPO will trigger at 10:00 AM on trading days. If you don't want to subscribe to new shares, delete stagging.py or don't start the "trading service".

![](img/11.jpg)

## IX. Stock Attention

Supports stock attention, highlighting stocks in various modules (including) at the top.

## X. Support Batch Processing


Can perform indicator calculations, stock selection, and backtesting based on time periods, enumerated dates, and current dates. Supports intelligent recognition of trading days, and can input any date.

Specific execution settings:
```
------Overall job, supports batch processing------
Current time job python execute_daily_job.py
Single time job python execute_daily_job.py 2022-03-01
Enumerated time job python execute_daily_job.py 2022-01-01,2021-02-08,2022-03-12
Interval time job python execute_daily_job.py 2022-01-01 2022-03-01

------Single function job, supports batch processing, backtest data automatically filled to the current
Real-time job python basic_data_daily_job.py
Non-real-time job python basic_data_other_daily_job.py
Indicator data job python indicators_data_daily_job.py
K-line pattern job klinepattern_data_daily_job.py
Strategy data job python strategy_data_daily_job.py
Backtest data python backtest_data_daily_job.py
```

## XI. Database Design

Data storage uses a database design, which can save historical data and perform extended analysis, statistics, and mining on the data. The system automatically creates databases and tables, and encapsulates batch updates and inserts data, making it easy to extend business.

![](img/07.jpg)

## XII. Web Design

Uses web design for visualization results. Encapsulates the display, adding new business forms, and only needs to configure the view dictionary to automatically appear business visualization interfaces, making it easy to extend business functions.

## XIII. High Efficiency


Uses multi-threading and single instance sharing resources to effectively improve calculation efficiency. The total running time for tasks such as data acquisition, indicator calculation, pattern recognition, stock selection, and backtesting is about 4 minutes (for a regular laptop), and the higher the number of days, the higher the efficiency.


## XIV. Convenient Debugging

Important logs are recorded in stock_execute_job.log (data acquisition, processing, analysis), stock_web.log (web service), and stock_trade.log (trading service), making it convenient to debug and find problems.

![](img/08.jpg)


# Installation Instructions

This system supports Windows, Linux, and MacOS. It also creates a Docker image for easy installation.

Below are instructions for regular installation and Docker image installation.

## I. Regular Installation

It's recommended to install on Windows for easy operation and use of the system.

The following installation and operation are based on Windows.

### 1. Install Python

The project development uses Python 3.11. It's recommended to use the latest version.

```
(1) Download and install the installer from https://www.python.org/downloads/. Make sure to check the option to automatically set the environment variables.
(2) Configure a permanent global domestic mirror library (due to the wall, it's difficult to install the library file normally). Execute the following dos command:
python pip config --global set  global.index-url https://mirrors.aliyun.com/pypi/simple/
# If you only want to set it for the current user, you can omit the "--global" option
```
### 2. Install MySQL

It's recommended to use the latest version.

```
Download and install the installer from https://dev.mysql.com/downloads/mysql/.
```
### 3. Install Dependencies

All dependencies are the latest versions.

a. Install dependencies:

```
# Switch to the root directory of the system and execute the following command:
python pip install -r requirements.txt
```
b. If you want to upgrade the project dependencies to the latest version, you can do so by modifying the "==" in the requirements.txt file to ">=", and then executing the following command:

```
python pip install -r requirements.txt --upgrade
```

c. If you extend the project, you can generate the project dependencies by using the following method:

```
# Use pipreqs to generate the requirements.txt for the project dependencies

python pip install pipreqs
# If pipreqs is already installed, you can skip this step

python  pipreqs --encoding utf-8 --force ./ 
# The project is in utf-8 encoding
```

### 4. Install talib

```
First method. Install from pip
(1) Download and unzip ta-lib-0.4.0-msvc.zip from https://www.ta-lib.org/
(2) Unzip and place ta_lib in the root directory
(3) Download and install Visual Studio Community from https://visualstudio.microsoft.com/zh-hans/downloads/
(4) Build TA-Lib Library # Build TA-Lib Library
    ① Search for and open [Native Tools Command Prompt] in the Start menu (select 32-bit or 64-bit based on the operating system)
    ② Enter cd C:\ta-lib\c\make\cdr\win32\msvc
    ③ Build the library, enter nmake
(5) Installation completed.

Second method. Install from Anaconda
(1) Open Anaconda Prompt terminal.
(2) Enter the command line conda install -c conda-forge ta-lib in the terminal.
(3) Confirm whether to continue installation? Enter y to continue installation until completed
(4) Installation completed.
```
### 5. Install Navicat (Optional)

Navicat is a convenient database management tool that can also be used for manual data viewing, processing, analysis, and mining.

Navicat is a database management tool that can create multiple connections to manage databases such as MySQL, Oracle, PostgreSQL, SQLite, SQL Server, MariaDB, and MongoDB.

```
(1) Download and install the installer from https://www.navicat.com.cn/download/navicat-premium.

(2) Then download the crack patch: https://pan.baidu.com/s/18XpTHrm9OiLEl3u6z_uxnw, extract code: 8888, and crack it.
```
### 6. Configure the Database

Commonly modified information is the "database access password".

Modify the database.py related information:

```
db_host = "localhost"  # Database service host
db_user = "root"  # Database access user
db_password = "root"  # Database access password
db_port = 3306  # Database service port
db_charset = "utf8mb4"  # Database character set
```

### 7. Install Automated Trading (Optional)

```
1. Install the trading software
    1.1 General Tonghuashun client for brokers
        General Tonghuashun client:
        https://activity.ths123.com/acmake/cache/1361.html
    1.2 Special Tonghuashun client for brokers
        Find Tonghuashun special version on the broker's official website
        For example: Download GF's independent entrustment terminal (Tonghuashun version):
        http://www.gf.com.cn/softdownload/index?tab=1
2. Install tesseract (automated verification code recognition)
    1st method. Download and compile
        On the following page, select the corresponding version based on the operating system
        https://digi.bib.uni-mannheim.de/tesseract/
    2nd method. Compile from source code
        Download the source code: https://github.com/tesseract-ocr/tesseract
    注意：
        After installation, set the installation path to the PATH environment variable.
        Below are dos commands to set the PATH environment variable, run cmd as an administrator, and enter:
        setx /m PATH "%PATH%;C:\Program Files\Tesseract-OCR"
3. Set trading configuration   
    3.1. Modify trade_client.json
        "user": "888888888888",               # Trading account
        "password": "888888",                 # Trading password
        "exe_path": "C:/gfzqrzrq/xiadan.exe"  # Trading software path
    3.2. Modify trade_service.py
        broker = 'gf_client' # This is GF
        详情参阅usage.md，配置对应券商
```

### 8. Running Instructions

#### 8.1. Execute Data Acquisition, Processing, Analysis, and Recognition

Supports batch processing. For details, see the comments in run_job.bat.

It's recommended to add this to the task schedule on weekdays at 17:00.

**Data acquisition and processing principles:**

1) Stocks with no historical data at the opening and no historical data at the closing: comprehensive stock screening, daily stock data, stock fund flows, stock dividends and distributions, dragon-tiger lists, daily ETF data;

2) Stocks with historical data at the closing and no historical data at the closing: stock indicator data, stock K-line patterns, stock strategy data;

3) Stocks with historical data 1-2 hours after the closing: block trades.

Run run_job.bat to obtain data for the current or previous trading day based on the above principles.

```

Run run_job.bat
```
If you want to see real-time data after the opening, you can run the following command, which is very fast, about 1 second:

```
# Real-time data job 
python basic_data_daily_job.py
```
#### 8.2. Start the Web Service

```
Run run_web.bat
```
After starting the service, open your browser and enter: http://localhost:9988/ to use the visualization functions of the system.

#### 8.3. Start the Trading Service

```
Run run_trade.bat
```

## II. Docker Image Installation

If you don't have a Docker environment, you can refer to: [VirtualBox Virtual Machine Installation of Ubuntu](https://www.ljjyy.com/archives/2019/10/100590.html), which also introduces the installation of Python and Docker. If you want to install Docker on Windows, you can search for it yourself.

### 1. Install the Database Image

If you already have an Msql or mariadb database, you can skip this step.

Run the following command:

**Special Reminder: The user executing the command must have root permissions. For example, on the ubuntu system, add sudo before the command. sudo docker......**

```
docker run -d --name InStockDbService \
    -v /data/mariadb/data:/var/lib/instockdb \
    -e MYSQL_ROOT_PASSWORD=root \
    library/mariadb:latest
```

### 2. Install the System Image

a. If you use the database image installed in step [1], run the following command:

```
docker run -dit --name InStock --link=InStockDbService \
    -p 9988:9988 \
    -e db_host=InStockDbService \
    mayanghua/instock:latest
```

b. If you already have an Msql or mariadb database, run the following command:

```
docker run -dit --name InStock \
    -p 9988:9988 \
    -e db_host=localhost \
    -e db_user=root \
    -e db_password=root \
    -e db_database=instockdb \
    -e db_port=3306 \
    mayanghua/instock:latest
```

docker -e parameter description:
```
db_host       # Database service host
db_user       # Database access user
db_password   # Database access password
db_database   # Database name
db_port       # Database service port
```
Configure parameters according to your actual database situation.

### 3. System Operation

After starting the container, it will automatically run, first initializing the data and starting the web service. Then, every hour, it will perform the "real-time data acquisition" task. At 17:30 every day, it will perform all data acquisition, processing, analysis, recognition, and backtesting tasks.

Open your browser and enter: http://localhost:9988/ to use the visualization functions of the system.

### 4. Historical Data

Historical data acquisition, processing, analysis, recognition, and backtesting, run the following command:

```
docker exec -it InStock bash 
cat InStock/instock/bin/run_job.sh
# View the comments in run_job.sh to select the job
------Overall job, supports batch processing------
Current time job python execute_daily_job.py
Single time job python execute_daily_job.py 2022-03-01
Enumerated time job python execute_daily_job.py 2022-01-01,2021-02-08,2022-03-12
Interval time job python execute_daily_job.py 2022-01-01 2022-03-01
------Single function job, supports batch processing, backtest data automatically filled to the current
Comprehensive stock screening job python selection_data_daily_job.py
Real-time job python basic_data_daily_job.py
2-hour post-closing job python backtest_data_daily_job.py
Non-real-time job python basic_data_other_daily_job.py
Indicator data job python indicators_data_daily_job.py
K-line pattern job klinepattern_data_daily_job.py
Strategy data job python strategy_data_daily_job.py
Backtest data python backtest_data_daily_job.py
First method:
python execute_daily_job.py 2023-03-01,2023-03-02
Second method:
Modify run_job.sh and then run bash InStock/instock/bin/run_job.sh
```

### 5. View Logs

Run the following command:

```
docker exec -it InStock bash 
cat InStock/instock/log/stock_execute_job.log
cat InStock/instock/log/stock_web.log
```

### 6. Docker Common Commands

```
docker container stop InStock InStockDbService
# Stop containers
docker container prune
# Recycle containers
docker rmi mayanghua/instock:latest library/mariadb:latest
# Delete images
```

For more details, see: [Docker Basics - II. Image and Container Basic Operations](https://www.ljjyy.com/archives/2018/06/100208.html)

### 7. Automated Trading

Currently only supported on Windows. Refer to the regular installation method, just install Python and dependencies, **no need to install MySQL, talib, etc.**

# Disclaimer

Stock market investment is risky, please be cautious. This system is only for learning and stock analysis, and the author is not responsible for investment profits and losses.

The tables in the system are third-party commercial components, which are used for learning and testing with the evaluation version.
