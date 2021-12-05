# map function
# def square(num):
#     return num ** 2

# my_nums = [1, 2, 3, 4, 5]
# #want to apply square function to the list
# for item in map(square, my_nums):
#     print(item)

# #another way is to use list keyword
# print(list(map(square, my_nums)))

# def splicer(mystring):
#     if len(mystring)%2 == 0:
#         return 'EVEN'
#     else:
#         return mystring[0]

# names = ['Andy', 'Eve', 'Sally']

# print(list(map(splicer, names)))

# filter function
# def check_even(num):
#     return num%2 == 0

# mynums = [1, 2, 3, 4, 5, 6]

# print(list(filter(check_even, mynums)))


#LAMBDA FUNCTION meant to be used just once
square = lambda num : num ** 2 #short form of a function
print(square(5))

#using lambda in map and filter
mynums = [1, 2, 3, 4, 5, 6]
print(list(map(lambda num:num ** 2, mynums)))

print(list(filter(lambda num:num % 2 == 0, mynums)))