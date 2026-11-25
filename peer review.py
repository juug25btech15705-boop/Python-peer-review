# Inventory Management System



inventory = {}


def add_item():
    name = input("Item name: ").lower()
    if name in inventory:
        print("Item already exists. Use update instead.")
        return
    qty = int(input("Quantity: "))
    price = float(input("Price: "))
    inventory[name] = [qty, price]
    print("Item added.")


def view_items():
    if len(inventory) == 0:
        print("Inventory is empty.")
        return
    print("\nName\tQty\tPrice")
    for name in inventory:
        print(name, "\t", inventory[name][0], "\t", inventory[name][1])


def update_item():
    name = input("Item name to update: ").lower()
    if name in inventory:
        inventory[name][0] = int(input("New quantity: "))
        inventory[name][1] = float(input("New price: "))
        print("Item updated.")
    else:
        print("Item not found.")


def delete_item():
    name = input("Item name to delete: ").lower()
    if name in inventory:
        del inventory[name]
        print("Item deleted.")
    else:
        print("Item not found.")


def search_item():
    name = input("Item name to search: ").lower()
    if name in inventory:
        print("Found ->", name, "Qty:", inventory[name][0], "Price:", inventory[name][1])
    else:
        print("Item not found.")


def low_stock():
    print("Items with quantity less than 5:")
    for name in inventory:
        if inventory[name][0] < 5:
            print(name, "->", inventory[name][0])


def total_value():
    total = 0
    for name in inventory:
        total = total + inventory[name][0] * inventory[name][1]
    print("Total inventory value:", total)


# Main menu (runs until user chooses Exit)
while True:
    print("\n--- INVENTORY MENU ---")
    print("1. Add item")
    print("2. View items")
    print("3. Update item")
    print("4. Delete item")
    print("5. Search item")
    print("6. Low stock items")
    print("7. Total inventory value")
    print("8. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_item()
    elif choice == "2":
        view_items()
    elif choice == "3":
        update_item()
    elif choice == "4":
        delete_item()
    elif choice == "5":
        search_item()
    elif choice == "6":
        low_stock()
    elif choice == "7":
        total_value()
    elif choice == "8":
        print("Thank you!")
        break
    else:
        print("Invalid choice.")
