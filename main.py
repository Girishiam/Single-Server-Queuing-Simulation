

import pandas as pd


import numpy as np

import warnings
warnings.filterwarnings('ignore')


custmerNumber = int(input())
np.random.seed(custmerNumber-1)
np.random.seed(custmerNumber)
c = 1  
utilization = {}
service_times = []





while c <= 1:
    if c == 1:
        inter_arrival_times = list(
            np.random.exponential(scale=1/1, size=custmerNumber))

    arrival_times = []
    departureTimes = []

    arrival_times = [0 for i in range(custmerNumber)]
    departureTimes = [0 for i in range(custmerNumber)]

    arrival_times[0] = round(inter_arrival_times[0], 2)

    for i in range(1, custmerNumber):
        arrival_times[i] = round(
            (arrival_times[i-1]+inter_arrival_times[i]), 2)


    if c == 1:
        service_times = list(np.random.exponential(scale=1/1.5, size=custmerNumber))

    departureTimes[0] = round((arrival_times[0]+service_times[0]), 2)


    for i in range(1, custmerNumber):
        formerFinish = departureTimes[:i]
        formerFinish.sort(reverse=True)
        formerFinish = formerFinish[:c]


        if i < c:
            departureTimes[i] = round(arrival_times[i] + service_times[i], 2)
        else:
            departureTimes[i] = round(
                (max(arrival_times[i], min(formerFinish))+service_times[i]), 2)



    total_times = [abs(round((departureTimes[i]-arrival_times[i]), 2))
                   for i in range(custmerNumber)]




    wait_times = [abs(round((total_times[i] - service_times[i]), 2))
                  for i in range(custmerNumber)]




    fullData = pd.DataFrame(list(zip(arrival_times, departureTimes, service_times, total_times, wait_times, inter_arrival_times)),
                        columns=['arrival_times', 'finish_times', 'service_times', 'total_times', 'wait_times', 'inter_arrival_times'])


    timeBetArr = list([0])
    customerDetails = ['simulation starts']


    for i in range(0, custmerNumber):
        timeBetArr.append(fullData['arrival_times'][i])
        timeBetArr.append(fullData['finish_times'][i])
        customerDetails.append('customer ' + str(i+1)+' arrived')
        customerDetails.append('customer ' + str(i+1)+' left')

    customerDetails = pd.DataFrame(list(zip(timeBetArr, customerDetails)),
                            columns=['time', 'Timeline']).sort_values(by='time').reset_index()
    customerDetails = customerDetails.drop(columns='index')

    customerDetails['n'] = 0
    
    x = 0


    for i in range(1, (2*custmerNumber)-1):
        if len(((customerDetails.Timeline[i]).split())) > 2:
            z = str(customerDetails['Timeline'][i]).split()[2]
        else:
            continue
        if z == 'arrived':
            x = x+1
            customerDetails['n'][i] = x
        else:
            x = x-1
            if x == -1:
                x = 0
            customerDetails['n'][i] = x



    t = list()
    for i in customerDetails.index:
        if i == (2*custmerNumber) - 2:
            continue
        if i < 2*custmerNumber:
            x = customerDetails.time[i+1]
        else:
            x = customerDetails.time[i]
        y = customerDetails.time[i]
        t.append(round((x-y), 2))

    t.append(0)
    customerDetails['tbe'] = t

    Pn = customerDetails.groupby('n').tbe.agg(sum)/sum(t)
    Tn = customerDetails.groupby('n').tbe.agg('count')

    customerDetails.n.describe()

    Ls = (sum(Pn*Pn.index))
    lqueue = sum((Pn.index[c+1:]-1)*(Pn[c+1:]))








    print(fullData.head(custmerNumber))
    print(customerDetails)
    print('Output:', '\n',

          'Average Delay: ', str(
              fullData.inter_arrival_times.mean()), '\n',

          ' Utilization (c): ', str((Ls-lqueue)/c), '\n',

          'Expected wait time in line (Wq):', str(
              fullData['wait_times'].mean()), '\n',

          'Expected number of customers in Queue (Lq):', str(lqueue), '\n',

          'Average number of customer in Queue:', lqueue/custmerNumber,'\n')

    c = c+1


