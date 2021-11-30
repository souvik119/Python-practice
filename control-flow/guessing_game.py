import random
num = random.randint(1,100)

print("WELCOME TO GUESS ME!")
print("I'm thinking of a number between 1 and 100")
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("If your guess is within 10 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
print("LET'S PLAY!")

guesses = []

while True:
    guess = int(input('Guess a number between 1 and 100 :'))

    if guess < 1 or guess > 100:
        print('OUT OF BOUNDS. Please try again')
        continue

    if guess == num:
        print(f'CONGRATULATIONS you guessed correct in {len(guesses) + 1} attempts')
        break

    if len(guesses) == 0:
        if abs(num - guess) <= 10:
            print('WARM')
        else:
            print('COLD')
    else:
        if abs(num-guess) < abs(num-guesses[-1]):
            print('WARMER')
        else:
            print('COLDER')

    #add guess to the list guesses
    guesses.append(guess)