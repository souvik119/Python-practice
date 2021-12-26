from collections import Counter
from collections import defaultdict
from collections import namedtuple

# COUNTER
# mylist = [1,1,1,1,1,1,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3]
# # can count frequency of each item using dictionary
# # Counter can do the same thing easily
# print(Counter(mylist))

# mylist = ['a', 'a', 'a', 'a', 'a', 10, 10]
# print(Counter(mylist))

# print(Counter('aaaab'))

# letters = 'aaabbbbccccccccdddddddddd'
# c = Counter(letters)
# print(c.most_common(2)) # prints top 2 most common letters
# # list unique items
# print(list(c))

# DEFAULT DICT
# normal dict:
# d = {'a':10}
# print(d)
# this will result in error as key does not exist
# print(d['WORNG KEY'])

# sometimes we want dict to asign default value to the key if not present instead of failing
# d = defaultdict(lambda:0) # 0 is the default value here
# d['correct key'] = 10
# print(d)
# print(d['wrong key!']) # this would have resulted in an error in regular dictionary

# NAMED TUPLE
Dog = namedtuple('Dog', ['age', 'breed', 'name'])
sammy = Dog(age=5, breed='Husky', name='Sam')
print(type(sammy))
print(sammy)
print(sammy[0])
print(sammy.name)