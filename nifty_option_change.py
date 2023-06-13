import nsepy as nse
from nsetools import Nse
import csv
import sys
import sched, time ,datetime
# import notify2
# notify2.init('vk')

# index = Nse()
# nifty = index.get_index_quote("NIFTY 50")
# print(nifty)
date = sys.argv[1]
curr_time = (str(datetime.datetime.now()).split(" ")[1]).split(".")[0]
# fil = open('trade_values_'+curr_time+'.csv', 'a')
fil = open('trade_values_change_'+str(date)+'.csv', 'a')
writer = csv.writer(fil)
trade_dict = {'i':0}
time_gap = 60

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

def normalize(d):
   raw = sum([abs(i) for i in list(d.values())])
   factor = 1.0/raw
   return {key:value*factor for key,value in d.items()}

def trade_nifty(symbols):

    final_result = [] ; final_v2={} ; p_change = {} ; pos= [] ; neg= []
    # print('Started................')
    for k,v in symbols.items():
        data = nse.live.get_quote(symbol=str(k))
        print(str(k),end ="\r")
        symbols[str(k)] = data['data'][0]['totalTradedVolume']
        change = data['data'][0]['pChange']
        p_change[str(k)] = float(change)

    symbols = dict([a, float(x.replace(",",""))] for a, x in symbols.items())
    symbols_norm =normalize(symbols)
    p_change_norm= normalize(p_change)

    for (k1,v1), (k2,v2) in zip(symbols_norm.items(), p_change_norm.items()):
        # print(k1,"#",v1,"#",v2)
        if k1==k2:
            result = v1*float(v2)
            final_result.append(result)
            final_v2[str(k1)] = float(v2)

    final_norm = normalize(final_v2)
    
    for i in list(final_norm.values()):
        if float(i)<0:
            neg.append(float(i))
        else:
            pos.append(float(i))

    return sum(final_result),pos,neg

def main(scheduler):

    try:
        scheduler.enter((time_gap)-0.5,0.5, main, (scheduler,))
        value,pos,neg = trade_nifty(symbols)
        ratio = sum(pos) + sum(neg)

        if abs(ratio)-abs(trade_dict['i'])>=0.15 or abs(ratio)-abs(trade_dict['i'])<=-0.15:
            print(" @@@@@@@@@@@@@@ Entry/Exit triggered @@@@@@@@@@@@@@")
            entry =["call" if ratio > trade_dict['i'] else "put"]
            # n = notify2.Notification(entry[0])
            print("{} {} {} {} {} {} {} {} {}".format(u'\u25B2',len(pos),u'\u25BC',len(neg),u'\u2192',round(ratio,4),round(trade_dict['i'],4),entry[0],"\U0001F600"))
            trade_dict['i'] = ratio

        print("{} {} {} {} {} {} ({})".format(u'\u25B2',len(pos),u'\u25BC',len(neg),u'\u2192',round(ratio,4),round(trade_dict['i'],4)))
        writer.writerow([ratio])
    except:
        pass
    
my_scheduler = sched.scheduler(time.time, time.sleep)
my_scheduler.enter(1,1, main, (my_scheduler,))
my_scheduler.run()