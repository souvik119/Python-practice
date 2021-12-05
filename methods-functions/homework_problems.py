# Write a function that computes the volume of a sphere given its radius
# def vol(r):
#     return (4/3) * 3.14 * (r ** 3)

# print(vol(2))

# Write a function that checks whether a number is in a given range (inclusive of high and low)
# def ran_check(num,low,high):
#     return num in range(low, high+1)

# print(ran_check(5,2,7))

# Write a Python function that accepts a string and calculates the number of upper case letters 
# and lower case letters
# def up_low(s):
#     alph_dict = {'upper':0, 'lower':0}
#     for char in s:
#         if char.isupper():
#             alph_dict['upper'] += 1
#         elif char.islower():
#             alph_dict['lower'] += 1
#         else:
#             pass
    
#     print("Original String : ", s)
#     print("No. of Upper case characters : ", alph_dict['upper'])
#     print("No. of Lower case Characters : ", alph_dict['lower'])

# s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
# print(up_low(s))

# Write a Python function that takes a list and returns a new list with unique elements of the first list
def unique_list(lst):
    return list(set(lst))

print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))

# Write a Python function to multiply all the numbers in a list.
def multiply(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

print(multiply([1,2,3,-4]))

# Write a Python function that checks whether a word or phrase is palindrome or not

def palindrome(s):
    s = s.replace(" ", "") # remove whitespace
    return s == s[::-1]

print(palindrome('nurses run'))
print(palindrome('abcba'))

# Write a Python function to check whether a string is pangram or not. 
# (Assume the string passed in does not have any punctuation)
import string
def ispangram(str1, alphabet=string.ascii_lowercase):
    alphabet_set = set(alphabet)
    str1 = str1.replace(" ", "") #get rid of whitespace
    str1 = str1.lower()
    str1 = set(str1)
    return str1 == alphabet_set

print(ispangram("The quick brown fox jumps over the lazy dog"))