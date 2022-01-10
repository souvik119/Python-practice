def rev_str(original_string):
    '''
    accepts a string
    returns the reverse
    '''
    reversed_string = ''
    for i in range(len(original_string)-1, -1, -1):
        reversed_string += original_string[i]

    return reversed_string


def main():
    print(rev_str('hello'))

if __name__ == '__main__':
    main()