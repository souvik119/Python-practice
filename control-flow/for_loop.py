mylist = [1,2,3,4,5,6,7,8,9,10]
# for num in mylist:
#     print(num)

# print only even numbers in the above list
for num in mylist:
    #check for even
    if num % 2 == 0:
        print(num)
    else:
        print(f'Odd number: {num}')

list_sum = 0
for num in mylist:
    list_sum += num

print(list_sum)

for letter in 'Hello World':
    print(letter)

#if you do not intend to use the variable inside the loop use _ as iterable
for _ in 'Hello World':
    print('Cool!')

mylist = [(1, 2), (3, 4), (5, 6), (7, 8)]
#this will demonstrate tuple unpacking
for a, b in mylist:
    print(a)

d = {'k1':1, 'k2':2, 'k3':3}
#by default only keys will be printed
for key, value in d.items():
    print(key, value)