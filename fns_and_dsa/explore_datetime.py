from datetime import datetime, timedelta

def display_current_datetime():
    # Get the current date and time
    current_date = datetime.now()
    # Format and print the date in a readable format
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    return current_date

def calculate_future_date(current_date, days_to_add):
    # Calculate the future date by adding days to the current date
    future_date = current_date + timedelta(days=days_to_add)
    # Format and print the future date
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future_date}")
    return future_date

def main():
    # Display the current date and time
    current_date = display_current_datetime()

    # Get the number of days to add from the user
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        # Calculate and display the future date
        calculate_future_date(current_date, days_to_add)
    except ValueError:
        print("Invalid input. Please enter an integer value.")

if __name__ == "__main__":
    main()

