import products
import store

def start():
    """
    Show the menu and get user input.
    If it's a valid option, return a pointer to the function to execute.
    Otherwise, keep asking the user for input.
    """
    print("\nMenu:")
    for key, value in FUNCTIONS.items():
        print(f"{key}. {value[1]}")

    # Input loop
    while True:
        try:
            choice = int(input("\nEnter choice (1-4): "))
            if choice in FUNCTIONS:
                return FUNCTIONS[choice][0]
        except ValueError as e:
            pass
        print("\033[31mTry again...\033[0m")


def command_list_all_products_in_store():
    pass

def command_show_total_amount_in_store():
    pass


def command_make_an_order():
    pass

"""
Function Dispatch Dictionary
"""
FUNCTIONS = {1: (command_list_all_products_in_store, "List all products in store"),
             2: (command_show_total_amount_in_store, "Show total amount in store"),
             3: (command_make_an_order, "Make an order"),
             4: (quit, "Exit"),
             }


def main():
    """
    # setup initial stock of inventory
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250)
                    ]
    best_buy = store.Store(product_list)
    """

    # The Main Menu loop
    while True:
        # Print menu and Get command from user
        choice_func = start()
        # Execute command
        print()
        choice_func()
        input("\nPress Enter to continue...")






if __name__ == "__main__":
    main()
