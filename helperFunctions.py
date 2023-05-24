
from stocksymbol import StockSymbol

def access_api():
    api_key = 'cf7959df-216f-461a-a735-0e3fe089d675'  
    ss =StockSymbol(api_key)
    return ss;

def get_exchange(symbol):
    ss = access_api()
    us_symbol_list = ss.get_symbol_list("us")
    for i in range(len(us_symbol_list)):
        if us_symbol_list[i]["symbol"]== symbol:
            ex_platform = us_symbol_list[i]['exchange']
    return ex_platform