import products


class Store:

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
        Order a shopping list
        :param shopping_list: list of products to order
        :return: total value of products ordered
        """
        total_amount = 0
        for product, quantity in shopping_list:
            total_amount += product.buy(quantity)
        return total_amount


def main():
    bose = products.Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = products.Product("MacBook Air M2", price=1450, quantity=100)

    # instance of a store
    best_buy = Store([bose, mac])

    pixel = products.Product("Google Pixel 7", price=500, quantity=250)
    best_buy.add_product(pixel)

    print(best_buy.products)

    bose = products.Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = products.Product("MacBook Air M2", price=1450, quantity=100)

    best_buy = Store([bose, mac])
    produkts = [(bose, 5), (mac, 30), (bose, 10)]
    price = best_buy.order(produkts)
    for product in produkts:
        product[0].show()
    print(f"Order cost: {price} dollars.")

    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250),
                    ]

    best_buy = Store(product_list)
    active_products = best_buy.get_all_products()
    print(best_buy.get_total_quantity())
    print(best_buy.order([(active_products[1], 1), (active_products[2], 2)]))


if __name__ == "__main__":
    main()
