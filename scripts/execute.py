from brownie import *
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

def lorenz(arr,imageFilename):
    """Draws lorenz curve"""

    ## first sort
    sorted_arr = arr.copy()
    sorted_arr.sort()
    # this divides the prefix sum by the total sum
    # this ensures all the values are between 0 and 1.0
    scaled_prefix_sum = sorted_arr.cumsum() / sorted_arr.sum()
    # this prepends the 0 value (because 0% of all people have 0% of all wealth)
    lorenz_curve = np.insert(scaled_prefix_sum, 0, 0)
    # we need the X values to be between 0.0 to 1.0
    plt.plot(np.linspace(0.0, 1.0, lorenz_curve.size), lorenz_curve)
    # plot the straight line perfect equality curve
    plt.plot([0,1], [0,1])
    plt.savefig(imageFilename)




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
    balances_end = getAccountBalances(cityCoin)

    print('\n\n')
    #Printing Statistics
    print("Initial Wealth distribution:")
    print("Gini index: ",gini(balances_start))
    print("Mean: ",np.mean(balances_start))
    print("Standard Deviation: ",np.std(balances_start))

    print('\n\n')
    print("Final Wealth distribution:")
    print("Gini index: ",gini(balances_end))
    print("Mean: ",np.mean(balances_end))
    print("Standard Deviation: ",np.std(balances_end))

    #Printing Lorenz Curves
    lorenz(balances_start,"matplotlib_start.png")
    lorenz(balances_end,"matplotlib_end.png")



