# def lesser_of_two_evens(a, b):
#     if (a%2 == 0) and (b%2 == 0):
#         if a<b:
#             return a
#         else:
#             return b
#     else:
#         if a > b:
#             return a
#         else:
#             return b

# print(lesser_of_two_evens(2,4))
# print(lesser_of_two_evens(2,5))

# #better way to implement above is to to use min and max

# def animal_crackers(text):
#     wordlist = text.split()
#     return wordlist[0][0] == wordlist[1][0]

# print(animal_crackers('Levelheaded Llama'))
# print(animal_crackers('Crazy Kangaroo'))

# def makes_twenty(a, b):
#     return a+b == 20 or a == 20 or b == 20

# print(makes_twenty(20,10))
# print(makes_twenty(12,8))
# print(makes_twenty(2,3))


# def old_macdonald(name):
#     if len(name) > 3:
#         return name[:3].capitalize() + name[3:].capitalize()
#     else:
#         return 'Name is too short'

# print(old_macdonald('macdonald'))

# def master_yoda(text):
#     return ' '.join(text.split()[::-1])

# print(master_yoda('I am home'))
# print(master_yoda('We are ready'))


# def almost_there(n):
#     return abs(100 - n) <= 10 or abs(200 - n) <= 10

# print(almost_there(90))
# print(almost_there(104))
# print(almost_there(150))
# print(almost_there(209))


# def has_33(nums):
#     for i in range(0, len(nums) - 1):
#         if nums[i] == 3 and nums[i+1] == 3:
#             return True
#     return False

# print(has_33([1, 3, 3]))
# print(has_33([1, 3, 1, 3]))
# print(has_33([3, 1, 3]))


# def paper_doll(text):
#     result = ''
#     for char in text:
#         result += char * 3
#     return result

# print(paper_doll('Hello'))
# print(paper_doll('Mississippi'))


# def blackjack(a,b,c):
#     if sum((a,b,c)) <= 21:
#         return sum((a,b,c))

#     elif sum((a,b,c)) > 21 and 11 in (a,b,c):
#         return sum((a,b,c)) - 10

#     else:
#         return 'BUST!'

# print(blackjack(5,6,7))
# print(blackjack(9,9,9))
# print(blackjack(9,9,11))


def summer_69(arr):
    total = 0
    flag = False
    for num in arr:
        if num == 6:
            flag = True
            continue
        elif flag == True and num != 9:
            continue
        elif num == 9:
            flag = False
            continue
        elif flag == False:
            total += num
    return total


print(summer_69([1, 3, 5]))
print(summer_69([4, 5, 6, 7, 8, 9]))
print(summer_69([2, 1, 6, 9, 11]))