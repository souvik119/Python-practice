def calculate_change(balance):
    '''
    Calculates how many denominations of dollars, quarters, pounds..
    Returns the denominations
    '''
    dollars = 0 # 1.00
    quarters = 0 # 0.25
    dimes = 0 # 0.10
    nickels = 0 # 0.05
    pennies = 0 # 0.01

    dollars = int(balance/1.00)
    balance -= dollars*1.00

    quarters = int(round(balance*100)/25)
    balance -= quarters*0.25

    dimes = int(round(balance*100)/10)
    balance -= dimes*0.10

    nickels = int(round(balance*100)/5)
    balance -= nickels*0.05

    pennies = int(round(balance*100)/1)
    balance -= pennies*0.01

    return dollars, quarters, dimes, nickels, pennies


def get_balance(cash, price):
    '''
    Returns the balance amount to be returned to customer
    '''
    return cash-price

def main():
    '''
    Wrapper function
    '''
    price = float(input('What is the price of the item: '))
    cash = float(input('How much did customer pay: '))
    balance = get_balance(cash, price)
    dollars, quarters, dimes, nickels, pennies = calculate_change(balance)
    print(f'Balance is : {balance:.2f}')
    print('Change is below : ')
    print(f'Dollars : {dollars}')
    print(f'Quarters : {quarters}')
    print(f'Dimes : {dimes}')
    print(f'Nickels : {nickels}')
    print(f'Pennies : {pennies}')


if __name__ == '__main__':
    main()