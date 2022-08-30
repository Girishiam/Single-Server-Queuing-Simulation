import simpy
import numpy as np



def generate_interarrival():
    return np.random.exponential(1/ncustomer)


def generate_service():
    return np.random.exponential(1/ncustomer)


def care_run(env,servers):
    i=0
    while True:

        if i==ncustomer:
            break
        else:
            i+=1
            yield env.timeout(generate_interarrival())
            env.process(customer(env,i, servers))


wait_t = []
service_time = []
def customer(env, customer ,servers):
    with servers.request() as request:
        t_arrival = env.now
        print(env.now, ' Customer {} Arrives'.format(customer))
        yield request
        print(env.now, 'Customer {} is being served'.format(customer))
        yield env.timeout(generate_service())
        print(env.now, 'Customer {} Departs'.format(customer))
        t_depart = env.now
        wait_t.append(t_depart - t_arrival)
        service_time.append(t_depart + t_arrival)

busy_server = []
queue_length = []
def observation(env,servers):
    while True:
        busy_server.append(env.now)
        queue_length.append(len(servers.queue))
        yield env.timeout(0.5)


np.random.seed(1)

ncustomer = int(input())
env = simpy.Environment()
servers = simpy.Resource(env,capacity=1)
env.process(care_run(env,servers))
env.process(observation(env, servers))
env.run(until=ncustomer)


number_customer_in_queue = [x for x in queue_length if x != 0]
average_number_ofcustomer_queue = (len(number_customer_in_queue))/ncustomer
print("\n")
print("Avg Number of customer in queue : ", average_number_ofcustomer_queue)
average_delay = sum(wait_t)/len(wait_t)
print("Average Delay : ", average_delay)

utilization = ((sum(busy_server))/sum(service_time))/ncustomer
print("Average utilization of the server : ",utilization*100,"%")

import matplotlib.pyplot as plt


plt.figure()
plt.hist(wait_t)
plt.xlabel("Time(minute)")
plt.ylabel("Number of Customer")