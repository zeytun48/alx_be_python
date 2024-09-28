# shopping_list_manager.py

def display_menu():
    """
    Display the menu options for the shopping list manager.
    """
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    """
    Main function to manage the shopping list.
    """
    # Initialize an empty shopping list
    shopping_list = []

    while True:
        # Display menu options to the user
        display_menu()
        
        # Get the user's choice
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt the user to enter an item name and add it to the list
            item = input("Enter the item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"{item} has been added to the list.")
            else:
                print("Item name cannot be empty.")
        elif choice == '2':
            # Prompt the user to enter an item name and remove it from the list
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"{item} has been removed from the list.")
            else:
                print(f"{item} not found in the list.")
        elif choice == '3':
            # Display the shopping list
            if shopping_list:
                print("\nCurrent Shopping List:")
                for i, item in enumerate(shopping_list, start=1):
                    print(f"{i}. {item}")
            else:
                print("The shopping list is currently empty.")
        elif choice == '4':
            # Exit the program
            print("Goodbye!")
            break
        else:
            # Handle invalid menu choices
            print("Invalid choice. Please try again.")

# Run the main function if this script is executed
if __name__ == "__main__":
    main()

