# inventory.py

inventory = [
    {"name": "Coca Cola", "price": 2.00, "quantity": 5},
    {"name": "Snickers Bar", "price": 1.50, "quantity": 10},
    {"name": "Bag of Chips", "price": 1.25, "quantity": 7},
    {"name": "Bottle of Water", "price": 1.00, "quantity": 3},
]

# Define the function
def print_inventory(inventory):
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