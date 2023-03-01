# inventory.py

# A dictionary that stores the items in the vending machine as keys and their prices and quantities as values
inventory = {
    "Coca Cola": [2.0, 5],
    "Snickers Bar": [1.5, 10],
    "Bag of Chips": [1.25, 7],
    "Bottle of Water": [1.00, 3]
}

# Define the function
def print_inventory(inventory):
    # Initialize a counter for the item number
    counter = 1
    # Loop through the keys of the dictionary
    for item in inventory.keys():
        # Get the value of the current key as a list
        price_quantity = inventory[item]
        # Print the item number, name, price and quantity
        print(f"{counter}. {item} (${price_quantity[0]}) - {price_quantity[1]} left")
        # Increment the counter by one
        counter += 1
# print_inventory(inventory)

inventory2 = [
    {"name": "Coca Cola", "price": 2.00, "quantity": 5},
    {"name": "Snickers Bar", "price": 1.50, "quantity": 10},
    {"name": "Bag of Chips", "price": 1.25, "quantity": 7},
    {"name": "Bottle of Water", "price": 1.00, "quantity": 3},
]

# Define the function
def print_inventory2(inventory):
    # Initialize a counter for the item number
    counter = 1
    # Loop through the list of dictionaries
    for item in inventory:
        # Get the name, price and quantity of the current item
        name = item["name"]
        price = item["price"]
        quantity = item["quantity"]
        # Print the item number, name, price and quantity
        print(f"{counter}. {name} (${price}) - {quantity} left")
        # Increment the counter by one
        counter += 1
#print_inventory2(inventory2)