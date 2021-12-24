# Imagine you created a basic function
# def simple_func():
#   do simple stuff
#   return something

# Now you want to add more functionality 
# 1. Can add code to existing function - but prob cannot call this in old code because of changes in fucntion
# 2. Create new function with old code + new functionality - what if you want to remove this later

# Maybe a better way exists - on/off system to quickly add this new funcitonality
# Python has decorators allow add on extra funtionality to existing function
# use @ operator and placed on top of original function

# @some_decorator
# def original_func():
#     do simple stuff
#     return something


# def func():
#     return 1

# def hello():
#     return "Hello"

# greet = hello # assign func to a variable
# print(greet())

# even if heelo is deleted greet still points to hello function
# functions are objects that can be passed t other objects

# def hello(name='Jose'):
#     # functions greet and welcome are only valid inside hello since they are defined inside
#     print('The hello() function has been executed!')

#     def greet(): # defining another function inside one function 
#         return '\t this is the greet() function inside hello()'
    
#     def welcome():
#         return '\t this is the welcome() function inside hello()'

#     # print(greet()) # calling greet inside the hello function itself
#     # print(welcome())
#     # print('This is the end of hello function')
#     print('I am going to return a function')
#     if name == 'Jose':
#         return greet # returning a function here
#     else:
#         return welcome

# # hello()
# # welcome() # this will result in error since scope of welcome is inside hello
# # if we want to access welcome and greet outside the hello function then return them

# my_new_func = hello('Jose') # in this case greet function has been returned and assigned to my_new_func
# print(my_new_func())


# def cool():

#     def super_cool():
#         return 'I am very cool'

#     return super_cool # function super_cool is returned here

# some_func = cool()
# print(some_func())

# passing a function as argument

# def hello():
#     return 'Jose'

# def other(some_func): #some_func is a function as argument
#     print('Other code runs here!')
#     print(some_func())


def new_decorator(original_func): # originl_func as argument
    def wrap_func(): # this is the extra functionality
        print('Some extra code before the original function')
        original_func() # original function execution
        print('Some extra code after the original function')
    
    return wrap_func


# def func_needs_decorator():
#     print('I want to be decorated')

# use decorator on the function func_needs_decorator
# decoarted_func = new_decorator(func_needs_decorator)
# decoarted_func()

# this is a complicated way of decorating function, eaiser way of doing this:
@new_decorator
def func_needs_decorator():
    print('I want to be decorated')

func_needs_decorator()
