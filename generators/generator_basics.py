# allows us to generate a sequence of values over time
# use yield statement
# when called they dont returna function and exit
# generator functions will automatically suspend and resume execution
# advantage - instead of having to compute and store value up front computes one value at a time

# example - range()

# def create_cubes(n):
#     for x in range(n):
#         yield x**3 # more memory efficient

# for x in create_cubes(10): #instead of storing whole list only yield one number at a time
#     print(x)

# def gen_fib(n):
#     a = 0
#     b = 1
#     for i in range(n):
#         yield a
#         a,b = b,a+b

# for num in gen_fib(10):
#     print(num)

# def gensquares(n):
#     for x in range(n):
#         yield x**2

# for x in gensquares(10):
#     print(x)

import random

def rand_num(low, high, n):
    for x in range(n):
        yield random.randint(low, high)
    
for num in rand_num(1, 10, 12):
    print(num)