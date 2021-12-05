from random import shuffle

# example = [1, 2, 3, 4, 5, 6, 7]

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

def player_guess():
    guess = ''
    while guess not in ['0', '1', '2']:
        guess = input("Pick a number : 0, 1 or 2")
    
    return int(guess)

def check_guess(shuffled_list, guess):
    if shuffled_list[guess] == 'O':
        print('Correct')
    else:
        print('Wrong')
        print(shuffled_list)

original_list = [' ', 'O', ' ']
shuffled_list = shuffle_list(original_list)
guess = player_guess()
check_guess(shuffled_list, guess)