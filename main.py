import products
import store


def start():
    """
    Show the menu and get user input.
    If it's a valid option, return a pointer to the function to execute.
    Otherwise, keep asking the user for input.
    """
    # Input loop
    while True:
        print("\n    Store Menu")
        print("    ----------")
        for key, value in FUNCTIONS.items():
            print(f"{key}. {value[1]}")

        try:
            choice = int(input("\nPlease choice a number (1-4): "))
            if choice in FUNCTIONS:
                return FUNCTIONS[choice][0]
        except ValueError:
            pass
        print("\033[31mError with your choice! Try again...\033[0m")


def command_list_all_products_in_store():
    """
    list all active products in store
    :return: active products
    """
    active_products = best_buy.get_all_products()
    print("------")

    for key, value in active_products.items():
        print(f"{key}.{value.show()}")

    print("------")
    return active_products


def command_show_total_amount_in_store():
    """
    show total quantity of product in store
    :return:
    """
    print(f"Total of: {best_buy.get_total_quantity()} item in store")


def enter_choice_products(active_products):
    """
    enter choice products
    :param active_products: list of active products
    :return: choice products
    """
    while True:
        try:
            choice = input("\nWhich product # do you want? ")
            if choice.strip() == "":
                return None
            choice = int(choice)

            if choice in active_products.keys():
                return choice
        except ValueError:
            pass
        print("\033[31mError with your choice! Try again...\033[0m")


def enter_quantity():
    """
    enter quantity of product
    :return: quantity of product
    """
    while True:
        try:
            quantity = input("What amount do you want? ")
            if quantity.strip() == "":
                return None

            quantity = int(quantity)
            return quantity
        except ValueError:
            pass
        print("\033[31mTry again...\033[0m")


def command_make_an_order():
    """
    make an order
    """
    products_in_store = command_list_all_products_in_store()
    print("when you want to finish order, enter empty text.")
    shopping_list = []
    try:
        while True:
            choice = enter_choice_products(products_in_store)
            quantity = enter_quantity()
            if choice is None and quantity is None:
                break

            if choice is None or quantity is None:
                print("\033[31mError adding product!\033[0m")
                continue

            product_in_store = products_in_store[choice].get_quantity()
            for set_order in shopping_list:
                if set_order[0] == products_in_store[choice]:
                    product_in_store -= set_order[1]

            if 0 < quantity <= product_in_store:
                shopping_list.append((products_in_store[choice], quantity))
                print("Product added to list!")
            else:
                if product_in_store <= 0:
                    print(f"\033[31mThere are no more stock of product "
                          f"'{products_in_store[choice].name}' \033[0m")
                else:
                    print(
                        f"\033[31mQuantity of '{products_in_store[choice].name}' "
                        f"is greater than the current stock. max {product_in_store}\033[0m")

        total = store.Store.order(shopping_list)
        print("**********")
        print(f"Order made! Total payment: ${total}")
    except Exception as error:
        print(error)


# Function Dispatch Dictionary
FUNCTIONS = {1: (command_list_all_products_in_store, "List all products in store"),
             2: (command_show_total_amount_in_store, "Show total amount in store"),
             3: (command_make_an_order, "Make an order"),
             4: (quit, "Exit"),
             }

# setup initial stock of inventory
product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                products.Product("Google Pixel 7", price=500, quantity=250)
                ]
best_buy = store.Store(product_list)


def main():
    """
    main function
    """
    # The Main Menu loop
    while True:
        # Print menu and Get command from user
        choice_func = start()
        # Execute command
        choice_func()


if __name__ == "__main__":
    main()
