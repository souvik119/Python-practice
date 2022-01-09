import random

def coinToss(trails):
    '''
    accepts number of coin toss trials
    returns total heads and tails
    '''
    tosslist, heads, tails = [], 0, 0
    for i in range(trails):
        flip = random.randint(0,1)
        if flip == 0:
            heads += 1
            tosslist.append("Heads")
        else:
            tails += 1
            tosslist.append("Tails")
    
    print(tosslist)
    return heads, tails

def main():
    trails = int(input("How many times do you want to toss the coin: "))
    heads, tails = coinToss(trails)
    print(f"Total heads are : {heads}")
    print(f"Total tails are : {tails}")

if __name__ == '__main__':
    main()