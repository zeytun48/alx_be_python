# Function to display the menu options to the user
def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

# Main function that handles the shopping list operations
def main():
    shopping_list = []  # Start with an empty shopping list

    # Loop to continuously display the menu until the user decides to exit
    while True:
        display_menu()  # Display the menu
        choice = input("Enter your choice: ")  # Get the user's choice

        # Handle each menu option based on user input
        if choice == '1':
            item = input("Enter the item to add: ").strip()  # Prompt for item name and strip any extra spaces
            shopping_list.append(item)  # Add the item to the shopping list
            print(f"'{item}' has been added to the shopping list.")
        
        elif choice == '2':
            item = input("Enter the item to remove: ").strip()  # Prompt for item name to remove
            if item in shopping_list:
                shopping_list.remove(item)  # Remove the item if it exists in the list
                print(f"'{item}' has been removed from the shopping list.")
            else:
                print(f"Item '{item}' not found in the shopping list.")  # Notify if item not found

        elif choice == '3':
            if shopping_list:
                print("\nCurrent Shopping List:")
                for i, item in enumerate(shopping_list, 1):
                    print(f"{i}. {item}")  # Display each item in the shopping list
            else:
                print("The shopping list is currently empty.")  # Notify if the list is empty

        elif choice == '4':
            print("Goodbye!")  # Exit message
            break  # Exit the loop and terminate the program

        else:
            print("Invalid choice. Please try again.")  # Handle invalid menu choice

# Ensure that the main function is called only when the script is executed directly
if __name__ == "__main__":
    main()

