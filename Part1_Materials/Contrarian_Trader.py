# Disclaimer: Please run the following code only with your Paper Trading Account and NOT with a live trading account!!!

import pandas as pd
import yfinance as yf
from ib_insync import *
#util.startLoop()


df = pd.read_csv(r"INSERT YOUR FILEPATH HERE", header = [0, 1], index_col = 0, parse_dates = [0])

symbols = df.Close.columns.to_list()
symbols.remove("^DJI")

perf = pd.Series(dtype = float)

count = 1
for symbol in symbols:
    try:
        fast_info = yf.Ticker(ticker = symbol).get_fast_info() # updated
        prc_chg = fast_info["last_price"] / fast_info["regularMarketPreviousClose"] - 1 
        perf.loc[symbol] = prc_chg
        print(count, end = '\r')
        count += 1
    except Exception as e:
        print("{} not found".format(symbol))
print("Download complete.")

perf.sort_values(inplace = True)
perf.index.name = "symbol"

buy_stocks = 3 # buy the 3 worst performing stocks
sell_stocks = 3 # short sell the 3 best performing stocks
shares = 1 # one share per stock

perf.iloc[:buy_stocks] = shares
perf.iloc[-sell_stocks:] = -shares

target = pd.concat([perf.iloc[:buy_stocks], perf.iloc[-sell_stocks:]]).to_frame().reset_index()
target.columns = ["symbol", "position"]
print("", end='\n')
print("Target Positions:", end= '\n')
print(target, end=2*'\n')

ib = IB()
ib.connect()

pos = ib.positions()
df = util.df(pos)
if df is not None:
    df["symbol"] = df.contract.apply(lambda x: x.symbol)
    df["conID"] = df.contract.apply(lambda x: x.conId)
else: 
    df = pd.DataFrame(columns = ["symbol", "position"])

trades = pd.merge(target, df[["symbol", "position"]], "outer", on = "symbol", suffixes = ["_t", "_a"])
trades.fillna(0, inplace = True)
trades["trades"] = trades.position_t - trades.position_a 
trades = trades[trades.trades !=0].set_index("symbol").copy()

for symbol in trades.index:
    to_trade = trades.loc[symbol, "trades"]
    if to_trade > 0: 
        side = "BUY"
    elif to_trade < 0:
        side = "SELL"
    contract = Stock(symbol, "SMART", "USD")
    cds = ib.reqContractDetails(contract)
    if len(cds) == 0:
        print("No Contract for {} found.".format(symbol))
    elif len(cds) == 1:
        contract = cds[0].contract
        order = MarketOrder(side, abs(to_trade))
        trade = ib.placeOrder(contract, order)
        while not trade.isDone():
            ib.waitOnUpdate()
        if trade.orderStatus.status == "Filled":
            print("{} {} @ {}".format(side, symbol, trade.orderStatus.avgFillPrice))
        else:
            print("{} {} failed.".format(side, symbol))
    else:
        contract = cds[0].contract
        print("Multiple Contracts for {} found.".format(symbol))
        order = MarketOrder(side, abs(to_trade))
        trade = ib.placeOrder(contract, order)
        while not trade.isDone():
            ib.waitOnUpdate()
        if trade.orderStatus.status == "Filled":
            print("{} {} @ {}".format(side, symbol, trade.orderStatus.avgFillPrice))
        else:
            print("{} {} failed.".format(side, symbol))  
pos = ib.positions()
df = util.df(pos)
df["symbol"] = df.contract.apply(lambda x: x.symbol)
df["conID"] = df.contract.apply(lambda x: x.conId)
print("", end='\n')
print("NEW Positions:", end= '\n')
print(df[["symbol", "position"]])

ib.disconnect()
