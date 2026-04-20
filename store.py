import products


class Store:

    def __init__(self, product_list):
        self.products = product_list

    def add_product(self, product):
        if not isinstance(product, products.Product):
            raise TypeError("Product must be of type Product")
        self.products.append(product)


    def remove_product(self, product):
        if not isinstance(product, products.Product):
            raise TypeError("Product must be of type Product")
        self.products.remove(product)


    def get_total_quantity(self):
        return sum(product.get_quantity() for product in self.products)


    def get_all_products(self):
        active_products = []
        for product in self.products:
            if product.is_active():
                active_products.append(product)
        return active_products


    def order(self, shopping_list):
        total =0
        for product, quantity in shopping_list:
            total += product.buy(quantity)
        return total



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
    print(best_buy.order([(active_products[0], 1), (active_products[1], 2)]))


if __name__ == "__main__":
    main()
