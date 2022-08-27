"""
In this file we setup all the parameters needed for the whole simulation.


Distributions Configuration Attributes
--------------------------------------
name : Distribution Name,
min: Minimum value (when we have 'none' as a distribution this will be the only value),
max: Maximum value (not needed on Pareto, uniform),
mu : Mean value (used only on Normal distribution),
sigma: Standard Deviation (used only on Normal distribution)


Available Distributions [Needed attributes]
-------------------------
None: [name,min] 
Uniform: [name,min,max]
Pareto: [name,min]
Normal: [name,min,nax,mu,sigma] 


Events Configuration Attributes
--------------------------------------
Events can be either services or requests
------------------------------------------
name: The name of the corresponding service/request.
price: The cost of the service/request.


Other variables
----------------
path: The absolute path to the route of the project.
number_of_users: The number of users of our system

"""


path = '/home/chrisbele/blockchain'
number_of_users = 100


wealth_distribution = {
    'name': 'None',
    'min' : 10
}


requests_to_users_distribution = {
    'name': 'Uniform',
    'min' : 1,
    'max' : number_of_users,
}


services_to_users_distribution = {
   'name': 'Normal',
    'min' : 1,
    'max' : number_of_users,
    'mu': 50 ,
    'sigma': 10
}


events = [
    {
        'name': 'Empty smart bin',
        'occurances': 10000,
        'price': 1
    },
    {
        'name': 'Declare Parking Space',
        'occurances': 8000,
        'price': 1
    },
    {
        'name': 'Charge bike',
        'occurances': 5000,
        'price': 2
    },
     {
        'name': 'Rent Drone',
        'occurances': 3500,
        'price': 3
    },
    {
       'name': 'Share Energy',
        'occurances': 2000,
        'price': 5
    },
    {
       'name': 'Share Data',
        'occurances': 1000,
        'price': 8
    },
]



