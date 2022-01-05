def monthly_payment(principal, monthly_interest, term):
    '''
    Expects principal (amount borrowed), monthly interest rate and duration
    Returns monthly payment
    '''
    return (principal*(monthly_interest*((1+monthly_interest)**term)))/(1+monthly_interest)**(term-1)


def main():
    '''
    Wrapper function
    '''
    principal = float(input('How much did you borrow : '))
    interest = float(input('Enter annual interest rate : '))
    monthly_interest = interest/100/12
    duration = int(input('In how many years do you want to repay it : '))
    term = duration * 12
    payment = monthly_payment(principal, monthly_interest, term)
    print(f'${principal} borrowed at {interest} rate comes out to ${payment:.2f} per month when paid over {duration} years')


if __name__ == '__main__':
    main()