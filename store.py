import products


class Store:
    """
    Store the products
    """

    def __init__(self, product_list):
        self.products = product_list

    def add_product(self, product):
        """
        Add a product to the store
        :param product: product to add
        """
        if not isinstance(product, products.Product):
            raise TypeError("Product must be of type Product")
        self.products.append(product)

    def remove_product(self, product):
        """
        Remove a product from the store
        :param product: product to remove
        """
        if not isinstance(product, products.Product):
            raise TypeError("Product must be of type Product")
        self.products.remove(product)

    def get_total_quantity(self):
        """
        Get the total quantity of the store
        :return: the total quantity of the store
        """
        return sum(product.get_quantity() for product in self.products)

    def get_all_products(self):
        """
        Get all products
        :return: all active products
        """
        active_products = {}
        i = 1
        for product in self.products:
            if product.is_active():
                active_products[i] = product
                i += 1
        return active_products

    @staticmethod
    def order(shopping_list):
        """
        Order products
        :param shopping_list: list of products to order
        :return: total value of products ordered
        """
        total_amount = 0
        for product, quantity in shopping_list:
            total_amount += product.buy(quantity)
        return total_amount
