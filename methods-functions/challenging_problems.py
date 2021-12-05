# Write a function that takes in a list of integers and returns True if it contains 007 in order
# example :
# spy_game([1,2,4,0,0,7,5]) --> True
# spy_game([1,0,2,4,0,5,7]) --> True
# spy_game([1,7,2,0,4,5,0]) --> False

def spy_game(nums):
    desired_list = [0, 0, 7, 'x'] #extra x for avoiding index out of range when 007 condition is met
    for num in nums:
        if num == desired_list[0]:
            desired_list.pop(0) # deleting the first element of the desired list

    return len(desired_list) == 1

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))

# Write a function that returns the number of prime numbers that exist up to and including a given number

def count_primes(num):
    if num < 2:
        return 0
    prime_list = []
    for i in range(2, num+1):
        prime = True
        for j in range(2, i):
            if i % j == 0:
                prime = False
                break
        if prime == True:
            prime_list.append(i)

    return len(prime_list)

print(count_primes(100))