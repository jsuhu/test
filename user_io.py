# user_io.py
import inventory

# A function that gets the user's input of money and validates it
def get_money():
    # Ask the user to input the amount of money they have
    money = input("\nPlease enter the amount of money you have: $")

    # Try to convert the input to a float value
    try:
        money = float(money)
        # Check if the money is greater than or equal to zero
        if money >= 0:
            # Return the valid money value
            return money
        else:
            # Display an error message if the money is negative
            print("\nInvalid input. Money cannot be negative.")
            # Call the function again to get a valid input
            return get_money()
    except Exception as e:
        # Display an error message if the input is not a number
        print("\nInvalid input. Error:", e)
        # Call the function again to get a valid input
        return get_money()
#get_money()

# A function that gets the user's choice of item and validates it
def get_item(inventory):
    choice = input("\nPlease enter the number of the item you wish to purchase: ")
    try:
        choice = int(choice)
        # Check if the choice is valid (i.e., in the inventory dictionary)
        if choice in range(1, len(inventory.keys()) + 1):
            # Get a list of keys from the inventory dictionary
            keys = list(inventory.keys())
            # Get the key corresponding to the choice by indexing the list
            key = keys[choice - 1]
            # Return the key
            return key
        else:
            # Display an error message if the choice is invalid
            print("\nInvalid input. Item not available.")
            # Call the function again to get a valid input
            return get_item(inventory)
    except Exception as e:
        # Display an error message if the input is not a number
        print("\nInvalid input. Error:", e)
        # Call the function again to get a valid input
        return get_item(inventory)
    
#get_item(inventory.inventory)
