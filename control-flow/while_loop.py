# will continue to execute a block of code while some condition is true
# while (some boolean condition):
#    do something

# can also include else
# while (some boolean condition):
#   do something
# else:
#   do something else

# x = 0
# while (x < 5):
#     print(f'Current value of x is {x}')
#     x += 1
# else:
#     print('x is not less than 5')

# else will be executed even if while loop is not executed even once

# x = [1, 2, 3]

# for item in x:
#     pass #does nothing

# print('end of my script')

# mystring = 'Sammy'
# for letter in mystring:
#     if letter == 'a':
#         continue #move on to the next iteration
#     print(letter)

mystring = 'Sammy'
for letter in mystring:
    if letter == 'a':
        break #exists from the loop
    print(letter)

