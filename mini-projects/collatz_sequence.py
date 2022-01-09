# If n is even, divide it by 2
# If n is odd, multiply it by 3 and add 1
# Purpose is to reach 1

def collatz(num):
    '''
    Accepts a number > 1
    Returns the collatz sequence
    '''
    sequence = ''
    while num > 1:
        sequence += str(num) + ','
        if num%2:
            num = num*3 + 1
        else:
            num = num//2
    sequence += str(1)
    return sequence

def main():
    num = int(input("Enter a number greater than 1 : "))
    seq = collatz(num)
    print(f"Collatz sequence for {num} is : {seq}")

if __name__ == '__main__':
    main()