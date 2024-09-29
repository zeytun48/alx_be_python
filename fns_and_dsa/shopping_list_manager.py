def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []  # Initialize an empty list to store items

    while True:
        display_menu()  # Call the display_menu function
        try:
            choice = int(input("Enter your choice: "))  # Convert input to an integer
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            item = input("Enter the item to add: ").strip()
            shopping_list.append(item)  # Add item to the shopping_list
            print(f"'{item}' has been added to the list.")
        elif choice == 2:
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)  # Remove item from the shopping_list
                print(f"'{item}' has been removed from the list.")
            else:
                print(f"'{item}' not found in the list.")
        elif choice == 3:
            print("Current Shopping List:")
            for item in shopping_list:
                print(f"- {item}")  # Display all items in the shopping_list
        elif choice == 4:
            print("Goodbye!")
            break  # Exit the program
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

