import nsepy as nse
from nsetools import Nse
import csv

# index = Nse()
# nifty = index.get_index_quote("NIFTY 50")
# print(nifty)

fil = open('trade_values.csv', 'a')
writer = csv.writer(fil)

trade_values = []
symbols = {
    'ADANIENT':0,
    'ADANIPORTS' :0,
    'APOLLOHOSP' :0,
    'ASIANPAINT': 0,
    'AXISBANK' :0,
    'BAJAJ-AUTO':0,
    'BAJFINANCE':0,
    'BAJAJFINSV':0,
    'BPCL':0,
    'BHARTIARTL':0,
    'BRITANNIA':0,
    'CIPLA':0,
    'COALINDIA':0,
    'DIVISLAB':0,
    'DRREDDY':0,
    'EICHERMOT':0,
    'GRASIM':0,
    'HCLTECH':0,
    'HDFC':0,
    'HDFCBANK':0,
    'HDFCLIFE':0,
    'HEROMOTOCO':0,
    'HINDALCO':0,
    'HINDUNILVR':0,
    'ICICIBANK':0,
    'INDUSINDBK':0,
    'INFY':0,
    'ITC':0,
    'JSWSTEEL':0,
    'KOTAKBANK':0,
    'LT':0,
    # 'M&M':0,
    'MARUTI':0,
    'NESTLEIND':0,
    'NTPC':0,
    'ONGC':0,
    'POWERGRID':0,
    'RELIANCE':0,
    'SBILIFE':0,
    'SBIN':0,
    'SUNPHARMA':0,
    'TATAMOTORS':0,
    'TATASTEEL':0,
    'TCS':0,
    'TATACONSUM':0,
    'TECHM':0,
    'TITAN':0,
    'ULTRACEMCO':0,
    'UPL':0,
    'WIPRO':0
}

# data = nse.live.get_quote(symbol='RELIANCE')
# print(data)

def trade_nifty(symbols):

    final_result = []
    market_ratio = {}

    
    for k,v in symbols.items():
        data = nse.live.get_quote(symbol=str(k))
        # try:
        symbols[str(k)] = data['data'][0]['totalTradedVolume']
        t_buy = data['data'][0]['totalBuyQuantity']
        t_sell = data['data'][0]['totalSellQuantity']
        # ratio = float(t_buy.replace(",",""))/float(t_sell.replace(",",""))
        ratio = (float(t_buy.replace(",","")))/(float(t_sell.replace(",","")) + float(t_buy.replace(",","")))
        market_ratio[str(k)] = ratio
            # avg = (float(data['data'][0]['buyPrice1'].replace(",",""))+float(data['data'][0]['buyPrice2'].replace(",",""))+float(data['data'][0]['buyPrice3'].replace(",",""))+float(data['data'][0]['buyPrice4'].replace(",",""))+float(data['data'][0]['buyPrice5'].replace(",","")))/5
            # print("{} : {}".format(k,avg))
        # except:
        #     print(" Error in retrieving " ,k)

    symbols = dict([a, float(x.replace(",",""))] for a, x in symbols.items())
    factor=1.0/sum(symbols.values())
    symbols_norm = { k: v*factor for k, v in symbols.items()}

    for (k1,v1), (k2,v2) in zip(symbols_norm.items(), market_ratio.items()):
        if k1==k2:
            result = v1*v2
            final_result.append(result)

    return sum(final_result)


while(1):
    value = trade_nifty(symbols)
    print("ratio value : ",value)
    trade_values.append(value)
    writer.writerow([value])


