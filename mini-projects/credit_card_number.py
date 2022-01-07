# Validate a credit card number using Luhn's algo
# Starting from the rightmost digit, double every second digit
# If the result is greater than 10, i,e if the result is a two-digit number add the individual digits to make it a single digit
# Add all the digits together and find the sum. If the modulus of the sum is 0 or in other words if the sum is a multiple of 10, the credit card number is valid

def get_digits(n):
    '''
    Accepts a string n
    Returns a list of numbers made up of n
    '''
    return [int(d) for d in str(n)]

def luhn_checksum(card_num):
    '''
    Accepts a lits as card_num
    Implements Luhn's algo to validate card_num
    '''
    even_num = card_num[-2::-2]
    odd_num = card_num[-1::-2]
    checksum = 0

    # add odd digits as it is to the checksum
    checksum += sum(odd_num)

    # double even numbers and if number greater than 9 add the digits
    for num in even_num:
        prod = num * 2
        if prod > 9:
            checksum += sum(get_digits(prod))
        else:
            checksum += prod

    return checksum%10

def main():
    card_num_str = input("Please enter a credit card number without spaces : ")
    card_num = get_digits(card_num_str)
    if luhn_checksum(card_num) == 0:
        print('Valid')
    else:
        print('Invalid')

if __name__ == '__main__':
    main()