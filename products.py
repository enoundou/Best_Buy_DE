class Product:
    """
    Product class
    """

    def __init__(self, name, price, quantity):

        self.name = name
        try:
            if name is None:
                raise ValueError('Invalid Product Name')
            if price < 0.0:
                raise ValueError('Invalid Product Price')
            if quantity < 0 :
                raise ValueError('Invalid Product Quantity')
            if type(quantity) is not int:
                raise TypeError('Invalid Type of Product Quantity')
            self.price = price
            self.quantity = quantity
            self.active = self.quantity > 0
        except Exception as e:
            print(e)
            self.active = False

    def get_quantity(self):
        """
        :return: the quantity of the product
        """
        return self.quantity

    def set_quantity(self, quantity):
        """
        sets the quantity of the product
        :param quantity: quantity of the product
        """
        self.quantity = quantity

    def is_active(self):
        """
        :return: the active status of the product
        """
        return self.active

    def activate(self):
        """
        activates the product
        """
        self.active = True

    def deactivate(self):
        """
        deactivates the product
        """
        self.active = False

    def show(self):
        """
        shows the item
        :return: product show
        """
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity):
        """
        buys the product
        :param quantity: quantity of the product to buy
        :return: value of the purchased product
        """
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
