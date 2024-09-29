# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """
    Convert a Fahrenheit temperature to Celsius.
    """
    # Use the global conversion factor to convert
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Convert a Celsius temperature to Fahrenheit.
    """
    # Use the global conversion factor to convert
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

def main():
    try:
        # Prompt user for temperature value
        temperature_input = float(input("Enter the temperature to convert: "))

        # Prompt user to specify the unit (Celsius or Fahrenheit)
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        # Perform conversion based on the unit entered
        if unit == 'C':
            converted_temp = convert_to_fahrenheit(temperature_input)
            print(f"{temperature_input}°C is {converted_temp}°F")
        elif unit == 'F':
            converted_temp = convert_to_celsius(temperature_input)
            print(f"{temperature_input}°F is {converted_temp}°C")
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

# Run the main function
if __name__ == "__main__":
    main()

