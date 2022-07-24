from config import *
from utils import *
import csv


print('~~~Distribute Wealth~~~')
header = ['user', 'balance']
with open('../initial_wealth.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for i in range(number_of_users):
        if use_pareto_for_wealth_destribution:
            balance = 100 + pareto(1)*100
        else:
            balance = 100
        print('User ',i,' with balance ',balance)    
        writer.writerow([i,balance])


users_to_requests = []
users_to_services = []


# Gerenting Requests
print("~~~ Requests ~~~~")
for event in events:
    occurances = truncatedNormal(0,500,150,5)
    print('Ocuurances of',event['name'],': ',occurances)
    for i in range(occurances):
        user = np.round(np.random.uniform(0,number_of_users-1))
        users_to_requests.append({
            'user': user,
            'event': event
        })


# Gerenting services
print('\n\n\n')
print("~~~ Services ~~~~")
for event in events:
    occurances = pareto(1)
    print('Ocuurances of',event['name'],': ',occurances)
    for i in range(occurances):
        user = uniform(0,number_of_users-1)
        users_to_services.append({
            'user': user,
            'event': event
        })



# Maching requests to services
print('\n\n\n')
print('~~~Transactions~~~')
header = ['from', 'to', 'amount','name', 'label']
with open('../transactions.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    transactions = []
    for request in users_to_requests:
        for service in users_to_services:
            if request['event']['name'] == service['event']['name']:
                print(request['user'], 'send to ',service['user'], ' the amount of ',service['event']['price'])
                row = [request['user'],service['user'],service['event']['price'],service['event']['label']]
                writer.writerow(row)
                users_to_requests.remove(request)
                users_to_services.remove(service)
                break


