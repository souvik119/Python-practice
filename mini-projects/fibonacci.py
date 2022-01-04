# generates fibonacci sequence starting from 0, 1, ....

def fibonacci(n):
    '''
    Takes a number n and returns fibonacci sequence upto that number
    '''
    sequence = ''
    a = 0 # starting sequence
    b = 1 # 2nd number
    while a <= n:
        sequence += f'{str(a)},'
        a, b = b, a+b
    
    return sequence.rstrip(',') # remove ending ,

def main():
    '''
    wrapper function
    '''
    print(fibonacci(int(input('Till what number do you want fibonacci sequence: '))))

if __name__ == '__main__':
    main()
    
