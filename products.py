class Product:
    def __init__(self, name, price = float, quantity = int):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True
        try:
            if name is None:
                raise Exception('Invalid Product Name')
            if price < 0:
                raise Exception('Invalid Product Price')
            if quantity < 0:
                raise Exception('Invalid Product Quantity')
        except Exception as e:
            print(e)

    def get_quantity(self):
        return self.quantity


    def set_quantity(self, quantity):
        self.quantity = quantity


    def is_active(self):
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity):
        try:
            if quantity <= 0:
                raise Exception('Invalid Product Quantity')
            if quantity > self.quantity:
                raise Exception(f'There are only {self.quantity} items left to sell')
        except Exception as e:
            print(e)
            return None

        self.quantity -= quantity
        self.active = self.quantity > 0

        return quantity * self.price

def main():
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    bose.show()
    mac.show()

    bose.set_quantity(1000)
    bose.show()

if __name__ == "__main__":
    main()