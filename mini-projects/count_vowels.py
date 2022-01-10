def count_vowels(string):
    '''
    Accepts a string
    returns a dictionary with vowel counts
    '''
    count = {}
    for letter in string:
        if letter in 'aeiou':
            if letter not in count:
                count[letter] = 1
            else:
                count[letter] += 1
    
    return count

def main():
    print(count_vowels('hello'))

if __name__ == '__main__':
    main()