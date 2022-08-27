from config import *
from utils import *
import csv


# print('~~~Distribute Wealth~~~')
# header = ['user', 'balance']
# with open(path+'/scripts/initial_wealth.csv', 'w', encoding='UTF8', newline='') as f:
#     writer = csv.writer(f)
#     writer.writerow(header)

#     #The account 0 is responsible for the rewards.
#     writer.writerow([0,10000000000])

#     for i in range(1,number_of_users+1):
#         balance = distributionController(wealth_distribution)
#         print('User ',i,' with balance ',balance)    
#         writer.writerow([i,balance])

users_to_requests = []
users_to_services = []


# Gerenting Requests
for event in events:
    occurances = event['occurances']
    for i in range(occurances):
        user = distributionController(requests_to_users_distribution)  
        users_to_requests.append({
            'user': user,
            'event': event
        })


# Gerenting services
print('\n\n\n')
for event in events:
    occurances = event['occurances']
    for i in range(occurances):
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
    for request in users_to_requests[:]:
        for service in users_to_services[:]:
            if request['event']['name'] == service['event']['name']:
                print(request['user'], 'send to ',service['user'], ' the amount of ',service['event']['price'])
                row = [request['user'],service['user'],service['event']['price']]
                writer.writerow(row)
                users_to_requests.remove(request)
                users_to_services.remove(service)
                break

