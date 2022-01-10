def fizzbuzz():
    '''
    Prints number from 1 to 100
    if number is multiple of 3 print fizz
    if number is multiple of 3 print buzz
    if number is multiple of 3 and 5 print fizzbuzz
    '''
    for i in range(1,101):
        if i%3 == 0  and i%5 == 0:
            print('fizzbuzz')
        elif i%3 == 0:
            print('fizz')
        elif i%5 == 0:
            print('buzz')
        else:
            print(i)

def main():
    fizzbuzz()

if __name__ == '__main__':
    main()