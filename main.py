# Inventory Management System

inventory = []
next_id = 1101


# 1. Add Item
def add_item():
    global next_id

    name = input("Enter item name: ")

    try:
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price: "))

        if quantity < 0 or price < 0:
            print("Invalid quantity or price.")
            return

        item = {
            "id": next_id,
            "name": name,
            "quantity": quantity,
            "price": price
        }

        inventory.append(item)

        print("Item added successfully!")
        print(item)

        next_id += 1

        if quantity < 5:
            print("Low stock alert:", name, quantity)

    except ValueError:
        print("Invalid input! Enter valid numbers.")


# 2. View All Items
def view_items():
    if not inventory:
        print("Inventory is empty.")
        return

    print("\nID     Name       Quantity    Price")
    print("------------------------------------")

    for item in inventory:
        print(
            item["id"], " ",
            item["name"], " ",
            item["quantity"], " ",
            item["price"]
        )


# 3. Update Item
def update_item():
    item_id = int(input("Enter Item ID to update: "))

    for item in inventory:
        if item["id"] == item_id:

            print("Item found:", item["name"])

            name = input("Enter new name: ")
            quantity = int(input("Enter new quantity: "))
            price = float(input("Enter new price: "))

            if quantity < 0 or price < 0:
                print("Invalid quantity or price.")
                return

            item["name"] = name
            item["quantity"] = quantity
            item["price"] = price

            print("Item updated successfully!")
            return

    print("Item ID", item_id, "not found.")


# 4. Delete Item
def delete_item():
    item_id = int(input("Enter Item ID to delete: "))

    for item in inventory:
        if item["id"] == item_id:
            inventory.remove(item)
            print("Item", item["name"], "deleted.")
            return

    print("Item ID", item_id, "not found.")


# 5. Search Item
def search_item():
    item_id = int(input("Enter Item ID to search: "))

    for item in inventory:
        if item["id"] == item_id:
            print("Item found:", item)
            return

    print("Item not found.")


# 6. Total Stock Value
def total_stock_value():
    total = 0

    for item in inventory:
        total += item["quantity"] * item["price"]

    print("Total stock value:", total)


# 7. Low Stock Report
def low_stock_report():
    print("\nLow Stock Items (Quantity below 5):")

    found = False

    for item in inventory:
        if item["quantity"] < 5:
            print(
                item["id"], "|",
                item["name"], "| Qty:",
                item["quantity"]
            )
            found = True

    if not found:
        print("No low stock items.")


# Main Menu
while True:

    print("\n===== INVENTORY MANAGEMENT SYSTEM =====")
    print("1. Add Item")
    print("2. View Items")
    print("3. Update Item")
    print("4. Delete Item")
    print("5. Search Item")
    print("6. Total Stock Value")
    print("7. Low Stock Report")
    print("8. Exit")

    choice = input("Enter your choice: ")

    try:
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
            total_stock_value()

        elif choice == "7":
            low_stock_report()

        elif choice == "8":
            print("Thank you for using Inventory System!")
            break

        else:
            print("Invalid menu choice!")

    except ValueError:
        print("Please enter valid input.")