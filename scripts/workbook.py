# factor=1.0/sum(d.values())
# normalised_d = {k: v*factor for k, v in d.items() }
# 
# result = dict([a, float(x.replace(",",""))] for a, x in d.items())

# d={'a':-20, 'b':10,'c':40,'d':-30}
# print(sum([abs(i) for i in list(d.values())]))

# def normalize(d, target=1.0):
#    raw = sum([abs(i) for i in list(d.values())])
#    factor = target/raw
#    return {key:value*factor for key,value in d.items()}

# res = normalize(d)
# print(res)

# import nsepy as nse
# data = nse.live.get_quote(symbol='Mahindra & Mahindra Limited')
# print(data)
# for k,v in data['data'][0].items():
#     print('{} :--> {}'.format(k,v))

# import time , datetime
# curr_time = (str(datetime.datetime.now()).split(" ")[1]).split(".")[0]
# trading = {} 

# # print(time.time()-curr_time)
# print(time.time())
# import numpy as np
# import notify2
# import sched, time


# def do_something(scheduler): 
    # schedule the next call first
   #  print("Doing Stuff !!!!")
   #  scheduler.enter(4.5,0.5, do_something, (scheduler,))
    # then do your stuff
   #  print(np.random.randint(1,2))

# k = np.random.randint(1,2)
# if k==2:
#    n = notify2.Notification(k)
#    n.show()
    
# my_scheduler = sched.scheduler(time.time, time.sleep)
# my_scheduler.enter(1,1, do_something, (my_scheduler,))
# my_scheduler.run()

# print("{}: {} , {}: {}".format("\U0001F612",2,"\U0001F600",8))
# print("\U0001F612")

ratio = 0.7003 ; trade = 0.8448
if abs(ratio)-abs(trade)>=0.15 or abs(ratio)-abs(trade)<=-0.15:
    print(" @@@@@@@@@@@@@@ Entry/Exit triggered @@@@@@@@@@@@@@")