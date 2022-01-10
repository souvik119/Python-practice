class Product:
    '''
    Stores information about a particular product
    '''
    def __init__(self, id, price, quantity):
        self.id = id
        self.price = price
        self.quantity = quantity

    
class Inventory:
    '''
    Keeps track of various products
    '''
    def __init__(self):
        self.products = {} # inititalize products dictionary

    def add_product(self, product):
        self.products[product.id] = [product.price, product.quantity]

    def remove_product(self, product):
        del self.products[product.id]

    def sell_product(self, product):
        if self.products[product.id][1] > 1:
            self.products[product.id][1] -= 1
        else:
            print('Item not in stock')

    def stock_product(self, product):
        self.products[product.id][1] += 1

    def product_value(self, product):
        return self.products[product.id][0] * self.products[product.id][1]

    def list_inventory(self):
        for key,value in self.products.items():
            print(f'{key} details below : ')
            print(f'Price is {value[0]}')
            print(f'Quantity is {value[1]}')
            print('---------------------------------')

    def total_value(self):
        total = 0
        for key,value in self.products.items():
            total += value[0] * value[1]

        return total


def main():
    apple = Product(1, 5, 20)
    banana = Product(2, 3, 10)
    orange = Product(3, 2, 50)

    inventory1 = Inventory()
    inventory1.add_product(apple)
    inventory1.add_product(banana)
    inventory1.add_product(orange)

    inventory1.list_inventory()
    print(inventory1.total_value())


if __name__ == '__main__':
    main()