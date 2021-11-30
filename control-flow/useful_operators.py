#range operator

# only 1 number mean start from 0 and end at number - 1
# for num in range(10):
#     print(num)

# 2 numbers mean start at first end at last - 1
# for num in range(4, 10):
#     print(num)

# 3 numbers mean start, stop -1 and step
# for num in range(4, 10, 2):
#     print(num)

# can also create a list of the range
# print(list(range(0, 11, 2)))

# index_count = 0
# for letter in 'abcde':
#     print(f'{letter} is at index {index_count}')
#     index_count += 1


# word = 'abcde'
# for item in enumerate(word):
#     print(item)

# word = 'abcde'
# for index,letter in enumerate(word):
#     print(f'letter is {letter} and index is {index}')


# mylist1 = [1, 2, 3, 4, 5, 6]
# mylist2 = ['a', 'b', 'c']
# mylist3 = [100, 200, 300]

# for a, b, c in zip(mylist1, mylist2, mylist3):
#     print(a, b, c)

# print(list(zip(mylist1, mylist2, mylist3)))

# mylist = [10, 20, 30, 40, 50, 100]
# print(min(mylist))
# print(max(mylist))

# from random import shuffle
# mylist = [1,2,3,4,5,6,7,8,9,10]
# shuffle(mylist) # inplace
# print(mylist)

from random import randint
print(randint(0, 100))