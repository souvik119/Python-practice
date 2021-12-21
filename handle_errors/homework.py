try:
    for i in ['a', 'b', 'c']:
        print(i**2)
except:
    print('An error occured')


x = 5
y = 0

try:
    z = x/y
except:
    print('An error occured')
finally:
    print('All Done.')


def ask():
    while True:
        try:
            num = int(input('Input an integer: '))
        except:
            print('An error occured! Please try again!')
            continue
        else:
            print(f'Thank you, your number squared is: {num ** 2}')
            break

ask()