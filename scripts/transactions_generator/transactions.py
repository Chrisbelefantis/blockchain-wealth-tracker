from config import *
from utils import *
import csv


print('~~~Distribute Wealth~~~')
header = ['user', 'balance']
with open(path+'/scripts/initial_wealth.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for i in range(number_of_users):
        balance = distributionController(wealth_distribution)
        print('User ',i,' with balance ',balance)    
        writer.writerow([i,balance])

users_to_requests = []
users_to_services = []


# Gerenting Requests
print("~~~ Requests ~~~~")
for event in events:
    occurances = distributionController(occurances_of_requests_distribution)
    print('Ocuurances of',event['name'],': ',occurances)
    for i in range(occurances):
        user = distributionController(requests_to_users_distribution)  
        users_to_requests.append({
            'user': user,
            'event': event
        })


# Gerenting services
print('\n\n\n')
print("~~~ Services ~~~~")
for event in events:
    #occurances = pareto(1)*100
    occurances = distributionController(occurances_of_services_distribution)
    print('Ocuurances of',event['name'],': ',occurances)
    for i in range(occurances):
        #user = uniform(0,number_of_users-1)
        user = distributionController(services_to_users_distribution)
        users_to_services.append({
            'user': user,
            'event': event
        })



# Maching requests to services
print('\n\n\n')
print('~~~Transactions~~~')
header = ['from', 'to', 'amount','name']
with open(path+'/scripts/transactions.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    transactions = []
    for request in users_to_requests:
        for service in users_to_services:
            if request['event']['name'] == service['event']['name']:
                print(request['user'], 'send to ',service['user'], ' the amount of ',service['event']['price'])
                row = [request['user'],service['user'],service['event']['price']]
                writer.writerow(row)
                users_to_requests.remove(request)
                users_to_services.remove(service)
                break


