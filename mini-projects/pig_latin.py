def piglatin(sentence):
    '''
    Accepts a string
    returns pig latin version of the string
    '''
    pl_words = []
    words = sentence.split()
    vowels = 'aeiou'
    for word in words:
        if len(word) > 2 and word[0] not in vowels:
            pl_words.append(word[1:]+'-'+word[0]+'ay')
        else:
            pl_words.append(word+'-ay')
    
    return ' '.join(pl_words)

def main():
    print(piglatin('The quick ass jumped over lazy dog'))

if __name__ == '__main__':
    main()