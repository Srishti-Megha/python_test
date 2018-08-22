from nsepy import get_history
import datetime


# Moving average(closing price)
    
def moving_average(data, period):
    data = data.asfreq('1D', method = 'pad')
    
    moving_average = data['Close'].rolling(window=period).mean()
    

    return(moving_average)
    
    
#dummy variables
def vol_shock(data):
    cal = data["Volume"].pct_change()
    v = []
    i = -1
    for items in cal:
        i += 1
        if i == 0:
            v.append("nan")
            continue
        elif i > 0 and cal[i] > 10:
            v.append(0)
                
        elif i > 0 and cal[i] <= 10:
            v.append(1)
            
    return v

def price_shock(data):
    v1 = []
            
    for i in range (len(data["Close"])):
        if i != len(data["Close"])-1 and (data["Close"][i] - data["Close"][i+1])/data["Close"][i] > 2:
            v1.append(1)
                
        elif i != len(data["Close"])-1 and (data["Close"][i] - data["Close"][i+1])/data["Close"][i] <= 2:
            v1.append(0)
            
        elif i == len(data["Close"])-1:
            v1.append("nan")
            
    return v1





NIFTY = ["NIFTY IT"]
Stocks = ["INFY", "TCS"]

data_NIFTY = {}
data_Stocks = {}
moving_average_Stocks = {}
moving_average_NIFTY = {}


# data and moving average
for items in Stocks:
    data_Stocks[items] = get_history(symbol = items, start = datetime.date(2015,1,1), end = datetime.date(2015,3,1))
    moving_average_Stocks[items]  = moving_average(data_Stocks[items], 4)
    

for items in NIFTY:
    data_NIFTY[items] = get_history(symbol = items, start = datetime.date(2015,1,1), end = datetime.date(2015,1,10), index = True)
    moving_average_NIFTY[items]  = moving_average(data_NIFTY[items], 4)
    
# create dummy variables
for items in data_Stocks:
    data_Stocks[items]["Volume_Shocks"] = vol_shock(data_Stocks[items])
    data_Stocks[items]["Price_Shocks"] = price_shock(data_Stocks[items])
    
for items in data_NIFTY:
    data_NIFTY[items]["Volume_Shocks"] = vol_shock(data_NIFTY[items])
    data_NIFTY[items]["Price_Shocks"] = price_shock(data_NIFTY[items])
    
