def decimalToBinary(n):
    '''
    Accepts a binary number
    Returns decimal equivalent
    '''
    binary = ''
    while n>0:
        binary += str(n%2)
        n = n//2

    return binary[::-1]

def binaryToDecimal(n):
    '''
    Accepts a decimal number
    Returns binary equivalent
    '''
    decimal = 0
    i = 0
    while n != 0:
        decimal += (n%10)* pow(2,i)
        n = n//10
        i+=1
    return decimal


def main():
    dec = decimalToBinary(45)
    bin = binaryToDecimal(10101)
    print(dec)
    print(bin)

if __name__ == '__main__':
    main()
