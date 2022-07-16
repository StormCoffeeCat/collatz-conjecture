import math
import random

# Starting statement
print('This is a simple Collatz Conjecture path generator. \nThe rules are: \nIf the number is even, divide by two. \nIf the number is odd, multiply by three and add one')
rand = input('Would you like to choose a starting number (type "c") or would you like a random starting number between 1 and 1,000,000 (type "r")?')
rand = rand.lower()

# Determines the starting number
if rand == 'c':
    number = int(input('Please type an integer for the starting number'))
elif rand == 'r':
    number = random.randint(1,1000000)
    print('Your starting number is '+ str(number))
    
    # Solving algorithm
def solve(number):
    print(number)
    # Counts iterations
    iteration = 1
    while True:
        # Determines whether the number is odd or even
        if number % 2 == 0:
            # Divides by 2 then prints the output
            number = number/2
            print(int(number))
            iteration = iteration+1
        else:
            # Multiplies by 3 and adds 1, then prints the output
            number = number*3
            number=number+1
            print(int(number))
            iteration = iteration+1
            
        if number == 1:
            print('Your number went through {0} interations.'.format(iteration))
            break

solve(number)
