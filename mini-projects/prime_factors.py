# find prime factors of a number if any

def find_factors(n):
    '''
    returns a list of all factors of a number n
    '''
    factors = []
    for i in range(2,n):
        if n%i == 0:
            factors.append(i)

    return factors

def find_prime(n):
    '''
    Returns True if number is prime. else returns False
    '''
    for i in range(2,n):
        if n%i == 0:
            return False
    
    return True

def main():
    '''
    Wrapper function
    '''
    num = int(input('Enter a number to find its prime factors: '))
    factors = find_factors(num)
    if factors == []:
        print('No factors')
    else:
        print(f'All factors are : {factors}')
        print(f'prime factors are : ')
        for factor in factors:
            if find_prime(factor):
                print(factor)

if __name__ == '__main__':
    main()