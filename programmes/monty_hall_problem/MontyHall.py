## Monty Hall Problem
# Let’s Make a Deal
# The game is then played as follows: 
# You get to choose a door. Say, for the sake of argument that you pick door number 2. 
# If the car is behind door 2, then you win the car, otherwise you win nothing. So far, so 
# good.
#
# Now comes the interesting bit. Obviously, at least one of the two remaining doors 
# doesn’t have a car behind it. Now, Monty knows which door has the car, and he 
# reveals one of the doors that you didn’t choose that doesn’t have the car. 
#
# Monty then asks you if you want to switch from the door you have chosen to the other 
# closed door. Do you want to change your choice in the hope that you will increase 
# your chance of winning the car? 
#
# Simulation 
# Write a function simulate() that runs 1000 iterations of a simulation of the Monty Hall 
# problem and so empirically verify the probabilities that we have just calculated.  
# The function should count how many times you win the car in a variable, K, and then 
# return K divided by the number of iterations, N. 
#
# Python includes the built-in function randint(). This generates random integers in the 
# range specified by the function arguments, so: 
#          randint(1,3) 
# with return a random integer in the range 1 to 3 (which is exactly what you will need 
# in order to pick a random door). 
#
# You will also have to simulate the actions of Monty Hall. Sometimes these actions 
# will be deterministic, at other times they will be stochastic (random). Recall that we 
# saw both types of action when we constructed the truth-table.  
#
# Once the “Monty-simulator” has picked a door, flip your choice to the remaining door. 
# If that matches the true location then you should increment K, otherwise not. 
# When you run this 1000 times, the output from your function should be approximately 
# equal to 2/3.

from random import randint

N = 1000

def simulate(N):
    K = 0
    ###insert your code here###
    return float(K) / float(N)

print simulate(N)
