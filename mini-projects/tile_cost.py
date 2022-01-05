def tile_cost(width, length, cost):
    '''
    Accepts arguments of width, length and cost of the tile
    Returns cost to tile whole area
    '''
    return width*length*cost

def main():
    '''
    Wrapper function
    '''
    width = float(input('Enter width : '))
    length = float(input('Enter length : '))
    cost = float(input('Enter cost : '))
    total = tile_cost(width, length, cost)
    print(f'Cost to tile {width} x {length} floor is : {total}')


if __name__ == '__main__':
    main()