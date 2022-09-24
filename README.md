# Overview
The aim of this implementation is to measure wealth distribution on blockchain and it's behavior under different circumstances. Using solidity we create an ERC20 
token and after we generate an initial state for our system and realistic transactions we apply those to our blockchain with Brownie. The final step is to export 
indexes such the Gini and the Nakamoto index related to the initial and the final wealth distribution of our system.

All configurations are taking place on config.py file and according those the initial wealth distribution and the transactions are generated. From there the execute.py which is a brownie script is responsible for executing thoses transactions on blockchain and exporting the statistics.

# Architecture of our system

![Architecture of our system](https://github.com/Chrisbelefantis/blockchain-wealth-tracker/blob/master/assets/merged_architecture.png)

# Output Example

## Console Output

![Output Example](https://github.com/Chrisbelefantis/blockchain-wealth-tracker/blob/master/assets/output.png)


## Lorenz Curves

![Lorenz Curves](https://github.com/Chrisbelefantis/blockchain-wealth-tracker/blob/master/assets/lorenz_curves_example.png)

## Wealth Distribution

![Wealth Distribution](https://github.com/Chrisbelefantis/blockchain-wealth-tracker/blob/master/assets/wealth_distribution_example.png)
