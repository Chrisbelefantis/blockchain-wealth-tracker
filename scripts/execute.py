from brownie import *
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
import csv


def printAccounts(token):
    """Prints the balance of all accounts"""
    for account in accounts[1:]:
        print('Account Address: ',account.address,' CityCoin: ',token.balanceOf(account), 'Eth: ', account.balance())

def getAccountBalances(token):
    """Returns an numpy array with the accounts balances in CityCoin"""
    balances = np.ones((len(accounts),1), dtype=np.uint32)
    for i in range(len(accounts)):
        balances[i,0] = token.balanceOf(accounts[i])

    return balances[:,0]

def gini(arr):
    """Calculated Gini Index"""

    ## first sort
    sorted_arr = arr.copy()
    sorted_arr.sort()
    n = arr.size
    coef_ = 2. / n
    const_ = (n + 1.) / n
    weighted_sum = sum([(i+1)*yi for i, yi in enumerate(sorted_arr)])
    return coef_*weighted_sum/(sorted_arr.sum()) - const_

def lorenz(initial,final):
    """Prints the lorenz curves of the initial and the final wealth distribution """

    initial_sorted_arr = initial.copy()
    initial_sorted_arr.sort()

    final_sorted_arr = final.copy()
    final_sorted_arr.sort()

    initial_scaled_prefix_sum = initial_sorted_arr.cumsum() / initial_sorted_arr.sum()
    final_scaled_prefix_sum = final_sorted_arr.cumsum() / final_sorted_arr.sum()

    initial_lorenz_curve = np.insert(initial_scaled_prefix_sum, 0, 0)
    final_lorenz_curve = np.insert(final_scaled_prefix_sum, 0, 0)

    plt.plot(np.linspace(0.0, 1.0, initial_lorenz_curve.size), initial_lorenz_curve, color='r',label="Initial wealth distribution")
    plt.plot(np.linspace(0.0, 1.0, final_lorenz_curve.size), final_lorenz_curve, color='g',label="Final wealth distribution")
    plt.plot([0,1], [0,1],label="Even Wealth distribution")

    plt.legend()
    plt.savefig("lorenz_curve.png")



def main():

    #Deploying Token
    cityCoin = CityCoin.deploy({"from":accounts[0]})

    
    #Destributing CityCoin to all Accounts
    with open('/home/chrisbele/blockchain/scripts/initial_wealth.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader, None)
        for row in reader:
            user = int(float(row[0]))
            amount = int(float(row[1]))
            cityCoin.claimToken(amount,{'from':accounts[user]})


    printAccounts(cityCoin)
    balances_start = getAccountBalances(cityCoin)

    #Executing the transactions
    with open('/home/chrisbele/blockchain/scripts/transactions.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader, None)
        index = 0
        for row in reader:
            try:
                index+=1
                from_user = int(float(row[0]))
                to_user = int(float(row[1]))
                amount = int(float(row[2]))
                cityCoin.approve(accounts[from_user],amount,{'from':accounts[from_user]})
                cityCoin.transferFrom(accounts[from_user],accounts[to_user],amount,{'from' : accounts[from_user]})
                print('Transaction number:',index)
                print(row)
            except Exception as e:
                print(e.__class__," occured.")
        


    printAccounts(cityCoin)
    balances_end = getAccountBalances(cityCoin)

    #Printing Statistics
    print('\n\n')
    print("Initial Wealth distribution:")
    print("Gini index: ",round(gini(balances_start),4))
    print("Mean: ",round(np.mean(balances_start),4))
    print("Standard Deviation: ",round(np.std(balances_start),4))
    print("Skewness:", round(stats.skew(balances_start),4))
    print("kurtosis:", round(stats.kurtosis(balances_start),4))


    print('\n\n')
    print("Final Wealth distribution:")
    print("Gini index: ",round(gini(balances_end),4))
    print("Mean: ",round(np.mean(balances_end),4))
    print("Standard Deviation: ",round(np.std(balances_end),4))
    print("Skewness:", round(stats.skew(balances_end),4))
    print("kurtosis:", round(stats.kurtosis(balances_end),4))


    #Printing Lorenz Curves
    lorenz(balances_start,balances_end)


    #Bar graph with the distribution
    # index = np.arange(len(accounts))
    # bar_width = 0.35
    # fig, ax = plt.subplots()
    # initial = ax.bar(index, balances_start, bar_width,
    #             label="Initial Balance")
    # final = ax.bar(index+bar_width, balances_end,
    #              bar_width, label="Final Balance")
    # ax.legend()
    # plt.savefig("balances_bar.png")