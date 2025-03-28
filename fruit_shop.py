import os
import time

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

class FruitShop:
    def __init__(self):
        self.fruit_prices = {
            'O': {'name': 'Orange', 'price': 0},
            'A': {'name': 'Apple', 'price': 0},
            'P': {'name': 'Pear', 'price': 0}
        }

    # === Admin Auth ===
    def admin_login(self):
        for attempt in range(3):
            password = input("Enter admin password: ")
            if password == "password":
                return True
            else:
                print("Incorrect password.")
        print("Too many incorrect attempts. Returning to main menu.")
        return False

    # === Admin Menu ===
    def admin_menu(self):
        while True:
            clear_console()
            print("Admin Menu:")
            print("1. Set Fruit Prices")
            print("2. Add New Fruit")
            print("3. Remove Fruit")
            print("4. Back to Main Menu")

            choice = input("Select an option (1-4): ")

            if choice == '1':
                self.set_fruit_prices()
            elif choice == '2':
                self.add_fruit()
            elif choice == '3':
                self.remove_fruit()
            elif choice == '4':
                break
            else:
                print("Invalid option. Try again.")
                input("Press Enter to continue...")

    # === Admin Actions ===
    def set_fruit_prices(self):
        clear_console()
        print("Set today's fruit prices:\n")
        for key, value in self.fruit_prices.items():
            while True:
                try:
                    price_input = float(input(f"Enter price for {value['name']}: £"))
                    value['price'] = price_input
                    break
                except ValueError:
                    print("Please enter a valid number.")
        clear_console()
        print("Prices updated!\n")
        time.sleep(1)

    def add_fruit(self):
        clear_console()
        prefix = input("Enter a unique one-letter prefix (e.g. B for Banana): ").upper()

        if prefix in self.fruit_prices:
            print("This prefix already exists.")
            input("Press Enter to return...")
            return

        name = input("Enter the name of the fruit: ").capitalize()
        try:
            price = float(input(f"Enter the price for {name}: £"))
            self.fruit_prices[prefix] = {'name': name, 'price': price}
            print(f"{name} added successfully.")
        except ValueError:
            print("Invalid price input.")
        input("Press Enter to continue...")

    def remove_fruit(self):
        clear_console()
        print("Current fruits:")
        for key, value in self.fruit_prices.items():
            print(f"{key}: {value['name']}")

        prefix = input("Enter the prefix of the fruit to remove: ").upper()

        if prefix in self.fruit_prices:
            removed = self.fruit_prices.pop(prefix)
            print(f"{removed['name']} has been removed.")
        else:
            print("Invalid prefix.")
        input("Press Enter to continue...")

    # === Customer Flow ===
    def purchase_items(self, budget):
        cart = {}

        while budget > 0:
            clear_console()
            print(f"\nYour remaining budget: £{budget}")
            self.display_menu()
            choice = self.get_user_choice()

            if choice == 'Q':
                print("Thanks for visiting!")
                time.sleep(2)
                break

            if choice in self.fruit_prices:
                budget = self.process_purchase(choice, budget, cart)
                input("Press Enter to continue...")
            else:
                print("Invalid selection.")
                input("Press Enter to try again...")

        self.print_receipt(cart, budget)

    def display_menu(self):
        print("Items for sale:")
        for key, value in self.fruit_prices.items():
            print(f"{key}: {value['name']} - £{value['price']}")
        print("Q: Quit")

    def get_user_choice(self):
        return input("Select item (prefix letter) or Q to quit: ").upper()

    def process_purchase(self, choice, budget, cart):
        selected = self.fruit_prices[choice]
        price = selected['price']
        name = selected['name']

        if price > budget:
            print(f"Not enough budget for {name} (£{price})")
        else:
            print(f"Purchased {name} for £{price}")
            cart[name] = cart.get(name, 0) + 1
            budget -= price

        return budget

    def print_receipt(self, cart, budget):
        clear_console()
        if cart:
            print("🧾 Your receipt:\n")
            for item, quantity in cart.items():
                print(f"{item}: x{quantity}")
            print(f"\nRemaining budget: £{budget}")
        else:
            print("You didn't buy anything.")
        time.sleep(4)
        clear_console()

    # === Role Selection ===
    def set_user(self):
        clear_console()
        print("Welcome to greens!")
        user = input("Are you a customer or an admin? ").lower()
        if user == 'admin':
            if self.admin_login():
                self.admin_menu()
            self.set_user()
        else:
            while True:
                try:
                    budget = float(input("What is your budget today? £"))
                    break
                except ValueError:
                    print("Please enter a valid number.")
            self.purchase_items(budget)

# === Main ===
shop = FruitShop()
shop.set_user()
