# *args
# **kwargs

# need to accept arbitrary no of arguments without defining vars in func call

# def myfunc(a, b):
#     # returns 5% of the sum of a and b
#     return sum((a, b)) * 0.05

# print(myfunc(40, 60))

# in above case a and b are positional arguments

# def myfunc(*args):
#     #can treat args as a tuple
#     return sum(args) * 0.05

#can pass any number of args
# print(myfunc(40, 60))
# print(myfunc(40, 60, 100))

# def myfunc(**kwargs):
#     print(kwargs)
#     if 'fruit' in kwargs:
#         print(f'My fruit of choice is {kwargs["fruit"]}')
#     else:
#         print('I did not find anything')

# myfunc(fruit='apple', veggie='lettuce')

# args gives tuple
# kwargs gives dictionary

def myfunc(*args, **kwargs):
    print(args)
    print(kwargs)
    print(f'I would like to {"args[0]"} {kwargs["food"]}')

myfunc(10, 20, 30, fruit='orange', food='eggs', animal='dog')