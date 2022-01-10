def check_palindrome(string):
    '''
    Accepts a string
    Returns True if string is a palindrome
    Else returns False
    '''
    for i in range(0, int(len(string)/2)):
        if string[i] != string[len(string)-1-i]:
            return False
    
    return True

def main():
    print(check_palindrome('hello'))

if __name__ == '__main__':
    main()