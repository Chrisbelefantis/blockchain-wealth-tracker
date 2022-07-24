from brownie import *
import numpy
import web3
import csv

def printAccounts(token):
    for account in accounts[1:]:
        print('Account Address: ',account.address,' CityCoin: ',token.balanceOf(account), 'Eth: ', account.balance())

def main():

    #Deploying Token
    cityCoin = CityCoin.deploy({"from":accounts[0]})

    
    # Destributing CityCoin to all Accounts
    with open('/home/chrisbele/blockchain/scripts/initial_wealth.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader, None)
        for row in reader:
            user = int(float(row[0]))
            amount = int(float(row[1]))
            cityCoin.claimToken(amount,{'from':accounts[user]})


    printAccounts(cityCoin)

    # Executing the transactions
    with open('/home/chrisbele/blockchain/scripts/transactions.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader, None)
        try:
            for row in reader:
                from_user = int(float(row[0]))
                to_user = int(float(row[1]))
                amount = int(float(row[2]))

                cityCoin.approve(accounts[from_user],amount,{'from':accounts[from_user]})
                cityCoin.transferFrom(accounts[from_user],accounts[to_user],amount,{'from' : accounts[from_user]})

                print(row)
        except Exception as e:
            print(e.__class__," occured.")


    printAccounts(cityCoin)

    



