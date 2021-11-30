# unique way of quickly creating lists
# if using for loop with .append() to create list, list comp prob a good alternative

mystring = 'hello'
# mylist = []
# for letter in mystring:
#     mylist.append(letter)

# print(mylist)

# another way to do the same
# mylist = [letter for letter in mystring]
# print(mylist)

# mylist = [x for x in 'word']
# print(mylist)

# mylist = [x for x in range(11)]
# print(mylist)

#can also perform operations on the number
# mylist = [x**2 for x in range(11)]
# print(mylist)

#can also include if conditions
# mylist = [x**2 for x in range(11) if x%2 == 0]
# print(mylist)

# celcius = [0, 10, 20, 34, 5]
# fahrenheit = [(9/5) * temp + 32 for temp in celcius]
# print(fahrenheit)

# results = [x if x%2 == 0 else 'ODD' for x in range(11)]
# print(results)

mylist = [x*y for x in [2, 4, 6] for y in [1, 10, 1000]]
print(mylist)