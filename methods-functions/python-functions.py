# clean repeatable code is key to becoming effective programmer
# functions allow us to create blocks of code that can be easily executed many times

# when naming a function use snake casing i.e., name_of_function lower case

# def say_hello():
#     print("hello")
#     print("how")
#     print("you")

# say_hello()

# def say_hello(name='Default'):
#     print(f'Hello {name}')

# say_hello('Jose')
# say_hello()

# python is dynamically typed meaning no need to define what type a particular variable is

def add_num(num1, num2):
    return num1+num2

result = add_num(10, 20)
print(result)