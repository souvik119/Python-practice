'''
Number - Python has different types of numeric literals. Focus here will be on int and float types.
Integers are whole numbers +ve or -ve
Floating point numbers have decimal point in them

Strings - Immutable sequence of characters that is ordered

Lists - Mutable sequence of characters that is ordered

Tuples - Similar to lists but immutable

Dictionaries - Mutable unordered collection of objects that are stored by a key-value pairing
'''

print((((((4 ** 2) / 8) * 6) - 2) * 10) + 0.25)

'''
What is the value of the expression 4 * (6 + 5) = 44

What is the value of the expression 4 * 6 + 5 = 29

What is the value of the expression 4 + 6 * 5 = 34
'''

# What is the type of the result of the expression 3 + 1.5 + 4? float

'''
What would you use to find a number’s square root, as well as its square?
100 ** 0.5 - sqrt
100 ** 2 - sq
'''

'''
Given the string 'hello' give an index command that returns 'e'. 
s = 'hello'
print(s[1])

Reverse the string 'hello' using slicing
print(s[::-1]) because start:stop:step


Given the string 'hello', give two methods of producing the letter 'o' using indexing
print(s[4])
print(s[-1])
'''

'''
Build this list [0,0,0] two separate ways
l1 = [0] * 3
l1 = [0, 0, 0]

Reassign 'hello' in this nested list to say 'goodbye' instead
list3 = [1,2,[3,4,'hello']]
list3[2][2] = 'goodbye'

Sort the list below:
list4 = [5,3,4,6,1]
sorted(list4) this will create a new list with sorted values and return the same
list4.sort() this will sort the list in place and no return value
'''

'''
Using keys and indexing, grab the 'hello' from the following dictionaries:
d = {'simple_key':'hello'}
d['simple_key']

d = {'k1':{'k2':'hello'}}
d['k1']['k2']

d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
d['k1'][0]['nest_key'][1][0]

d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
d['k1'][2]['k2'][1]['tough'][2][0]


Can you sort a dictionary? Why or why not?
No because dictionary is not an ordered sequence
'''

'''
Tuples:
Tuples are immutable, once defined cannot be changed
t = (1, 2, 3)
'''

'''
Sets:
Sets do not allow duplicates
t = (1, 2, 3)

Use a set to find the unique values of the list below:
list5 = [1,2,2,33,4,4,11,22,3,3,2]
set(list5)
'''

'''
Boolean:
2 > 3 False
3 <= 2 False
3 == 2.0 False
3.0 == 3 True
4**0.5 != 2 False
What is the boolean output of the cell block below
l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]
l_one[2][0] >= l_two[2]['k1'] False
'''



