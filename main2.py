# main.py

# Import the inventory and user_io modules 
import inventory2
import user_io2

# Define a main function that runs the program 
def main():
    # Display a welcome message 
    print(f"\nWelcome to the Vending Machine!")

    while True:
        # Get the user's input of money 
        money = user_io2.get_money()

        # Print the inventory
        inventory2.print_inventory(inventory2.inventory)

        # Get the user's choice of item 
        item, choice = user_io2.get_item(inventory2.inventory)

        # Get the price and quantity of the chosen item from the inventory dictionary 
        price = inventory2.inventory[choice - 1]["price"]
        quantity = inventory2.inventory[choice - 1]["quantity"]

        # Check if there is enough quantity of the chosen item 
        if quantity > 0:
            # Check if the user has enough money to buy the chosen item 
            if money >= price:
                # Calculate the change 
                change = money - price

                # Print the change 
                print(f"You have inserted ${money}. Your change is ${change}.")
                print(f"\nThank you for your purchase! Enjoy your {item}!")
                # Update the quantity of the chosen item in the inventory dictionary 
                inventory2.inventory[choice - 1]["quantity"] -= 1
            else:
                # Display an error message if the user does not have enough money 
                print(f"You have inserted ${money}. You need ${price - money} more to buy this item.")
        else:
            # Display an error message if there is not enough quantity of the chosen item 
            print(f"Sorry, we are out of {item}.")
        stage = input("\nWould you like to buy another item? (y/n): ")
        if stage == "n":
            break
        elif stage == "y":
            continue
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
    print(f"\nThank you for using the Vending Machine!")

main()