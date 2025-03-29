import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def isItemExists(itemPrefixes, itemPrefix):
    for i in range(len(itemPrefixes)):
        if itemPrefixes[i] == itemPrefix:
            return i
    return -1

def displayMenu(itemPrefixes, itemPrices, n):
    print("\nAvailable items:")
    for i in range(n):
        print(f"{itemPrefixes[i]}: £{itemPrices[i]}")
    print("Q: Quit")

def withinBudget(budget, itemPurchased, itemPrefixes, itemPrices):
    index = isItemExists(itemPrefixes, itemPurchased)
    if index == -1:
        return False
    return itemPrices[index] <= budget

def getItemPrice(itemPurchased, itemPrefixes, itemPrices):
    index = isItemExists(itemPrefixes, itemPurchased)
    if index == -1:
        return -1
    return itemPrices[index]

def purchaseItem(budget, itemPurchased, itemPrefixes, itemPrices, cart):
    index = isItemExists(itemPrefixes, itemPurchased)
    if index == -1:
        print("Item not found.")
        return budget

    price = itemPrices[index]
    if price > budget:
        print(f"Not enough budget for item {itemPurchased} (£{price})")
    else:
        print(f"Purchased item {itemPurchased} for £{price}")
        cart[index] = cart.get(index, 0) + 1
        budget -= price
    return budget

def printReceipt(cart, itemPrefixes, itemPrices, remaining_budget):
    clear_console()
    print("\n🧾 Receipt:")
    if cart:
        for index in cart:
            quantity = cart[index]
            name = itemPrefixes[index]
            price = itemPrices[index]
            print(f"{name}: x{quantity} @ £{price} = £{price * quantity}")
        total_spent = sum(itemPrices[i] * qty for i, qty in cart.items())
        print(f"\nTotal spent: £{total_spent}")
        print(f"Remaining budget: £{remaining_budget}")
    else:
        print("You didn't buy anything.")
    input("\nPress Enter to exit...")

# === Main program ===
def main():
    itemPrefixes = []
    itemPrices = []
    cart = {}

    # Shop owner setup
    clear_console()
    num_items = int(input("How many items would you like to add? "))

    for i in range(num_items):
        clear_console()
        prefix = input(f"Enter prefix for item {i+1} (e.g. A, O, P): ").upper()

        if isItemExists(itemPrefixes, prefix) != -1:
            print("This item already exists! Skipping.")
            input("Press Enter to continue...")
            continue

        try:
            price = int(input(f"Enter price for item '{prefix}': £"))
        except ValueError:
            print("Invalid price. Skipping.")
            input("Press Enter to continue...")
            continue

        itemPrefixes.append(prefix)
        itemPrices.append(price)

    # Customer interaction
    clear_console()
    print("\n--- Customer Section ---")
    try:
        budget = int(input("Enter your budget: £"))
    except ValueError:
        print("Invalid budget amount.")
        return

    n = len(itemPrefixes)

    while budget > 0:
        clear_console()
        print(f"Current budget: £{budget}")
        displayMenu(itemPrefixes, itemPrices, n)

        itemPurchased = input("Select item to purchase (use prefix or Q to quit): ").upper()

        if itemPurchased == 'Q':
            print("Thanks for shopping!")
            input("Press Enter to view your receipt...")
            break

        if withinBudget(budget, itemPurchased, itemPrefixes, itemPrices):
            budget = purchaseItem(budget, itemPurchased, itemPrefixes, itemPrices, cart)
        else:
            print("Purchase failed. Either item doesn't exist or budget too low.")
            input("Press Enter to continue...")

    printReceipt(cart, itemPrefixes, itemPrices, budget)

if __name__ == "__main__":
    main()
