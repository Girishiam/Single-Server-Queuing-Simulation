from prettytable import PrettyTable
import random

# Seed
random.seed(20)
random.seed(20)
# No. of Customer
size = int(input())

# Series of customer
customer = [i for i in range(1, size+1)]

# Inter Arrival Time
inter_arrival_time = [random.randrange(1, 10) for i in range(size)]

# Service Time
service_time = [random.randrange(1, 10) for i in range(size)]

print(len(inter_arrival_time), len(service_time))

# Calculate arrival time
arrival_time = [0 for i in range(size)]

# initial
arrival_time[0] = inter_arrival_time[0]

for i in range(1, size):
    arrival_time[i] = inter_arrival_time[i]+arrival_time[i-1]


Time_Service_Begin = [0 for i in range(size)]
Time_Customer_Waiting_in_Queue = [0 for i in range(size)]
Time_Service_Ends = [0 for i in range(size)]
Time_Customer_Spend_in_System = [0 for i in range(size)]
System_ideal = [0 for i in range(size)]

Time_Service_Begin[0] = arrival_time[0]
Time_Service_Ends[0] = service_time[0]
Time_Customer_Spend_in_System[0] = service_time[0]
for i in range(1, size):

    Time_Service_Begin[i] = max(arrival_time[i], Time_Service_Ends[i-1])

    Time_Customer_Waiting_in_Queue[i] = Time_Service_Begin[i]-arrival_time[i]

    Time_Service_Ends[i] = Time_Service_Begin[i] + service_time[i]

    Time_Customer_Spend_in_System[i] = Time_Service_Ends[i] - arrival_time[i]

    if (arrival_time[i] > Time_Service_Ends[i-1]):
        System_ideal[i] = arrival_time[i]-Time_Service_Ends[i-1]
    else:
        System_ideal[i] = 0


x = PrettyTable()

column_names = ['Customer', 'InterArrivalTime', 'ArrivalTime', 'ServiceTime',
                'TimeServiceBegin', 'CustomerWaitinQueue', 'ServiceEnd', 'CustomerSpendSystem', 'SystemIdeal']
data = [customer, inter_arrival_time, arrival_time, service_time, Time_Service_Begin,
        Time_Customer_Waiting_in_Queue, Time_Service_Ends, Time_Customer_Spend_in_System, System_ideal]

length = len(column_names)

for i in range(length):
    x.add_column(column_names[i], data[i])

print(x)


Average_waiting_time = sum(Time_Customer_Waiting_in_Queue)/size


no_customer_who_are_waiting = len(
    list(filter(lambda x: x > 0, Time_Customer_Waiting_in_Queue)))
prob_customer_waiting = no_customer_who_are_waiting / size
Average_service_time = sum(service_time)/size
prob_ideal_server = sum(System_ideal) / Time_Service_Ends[size-1]
Average_Time_Between_Arrival = arrival_time[size-1] / (len(arrival_time) - 1)


average_waiting_time = sum(
    Time_Customer_Waiting_in_Queue) / no_customer_who_are_waiting


time_customer_spent = sum(Time_Customer_Spend_in_System)/size

print("Average waiting time : {:.2f}".format(Average_waiting_time))
print('-'*50)

print("Probability of customer were waiting : {:.2f}".format(
    prob_customer_waiting))
print('-'*50)

print("Average service time : {:.2f}".format(Average_service_time))
print('-'*50)


print("Average Delays : {:.2f}".format(
    Average_Time_Between_Arrival))
print('-'*50)

print("Average waiting time those who wait : {:.2f}".format(
    average_waiting_time))

list1 = input().split(" ")
list2 = input().split(" ")

p1, p1_quantity, p1_price = list1

p2, p2_quantity, p2_price = list2


# re = int(p1_quantity)*float(p1_price) + int(p2_quantity)*float(p2_price)
# print("VALOR A PAGAR: R$ "'{:.2f}'.format(re), end="\n")
# a, b, c = [int(x) for x in input().split()]
# abs_val = abs(a-b)
# maiorab = (((a+b)+abs_val*(a-b))/2)
# res = ((maiorab+c+abs(maiorab-c))/2)

# print(res, " eh o maior", end='\n')
