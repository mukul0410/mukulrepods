menu = {
    "Pizza": 250,
    "Burger": 150,
    "Pasta": 200,
    "Coke": 50
}  

orders = {}

while True:
    print("1. Show Menu")
    print("2. Take Order")
    print("3. Update Menu")
    print("4. Generate Bill")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        print("\n----- MENU -----")
        for item, price in menu.items():
            print(f"{item}: ₹{price}")

    elif choice == '2':
        print("\n----- PLACE ORDER -----")
        print("Type 'done' when finished.\n")
        for item, price in menu.items():
            print(f"{item}: ₹{price}")
        while True:
            item = input("Enter item name: ").title()
            if item.lower() == 'done':
                break
            if item in menu:
                qty = int(input(f"Enter quantity for {item}: "))
                if item in orders:
                    orders[item] += qty
                else:
                    orders[item] = qty
            else:
                print("Item not found in menu. Please try again.")

    elif choice == '3':
        print("\n----- UPDATE MENU -----")
        action = input("Do you want to add or remove an item? (add/remove): ").lower()
        if action == "add":
            new_item = input("Enter item name: ").title()
            new_price = int(input(f"Enter price for {new_item}: "))
            menu[new_item] = new_price
            print(f"{new_item} added to the menu.")
        elif action == "remove":
            remove_item = input("Enter item name to remove: ").title()
            if remove_item in menu:
                del menu[remove_item]
                print(f"{remove_item} removed from the menu.")
            else:
                print("Item not found in menu.")

    elif choice == '4':
        print("\n----- BILL -----")
        total = 0
        for item, qty in orders.items():
            item_total = menu[item] * qty
            print(f"{item} x {qty} = ₹{item_total}")
            total += item_total
        print(f"Total Amount: ₹{total}")

    elif choice == '5':
        print("Thank you for visiting!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 5.")