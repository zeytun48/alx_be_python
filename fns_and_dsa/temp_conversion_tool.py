# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """
    Convert a Fahrenheit temperature to Celsius using the global conversion factor.
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Convert a Celsius temperature to Fahrenheit using the global conversion factor.
    """
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

def main():
    try:
        # Prompt the user to enter a temperature value and ensure it's numeric
        temperature_input = float(input("Enter the temperature to convert: "))

        # Prompt the user to specify if the temperature is in Celsius or Fahrenheit
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        # Perform the conversion based on the user's input
        if unit == 'C':
            converted_temp = convert_to_fahrenheit(temperature_input)
            print(f"{temperature_input}°C is {converted_temp}°F")
        elif unit == 'F':
            converted_temp = convert_to_celsius(temperature_input)
            print(f"{temperature_input}°F is {converted_temp}°C")
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError:
        # Handle the case when a non-numeric value is entered
        print("Invalid temperature. Please enter a numeric value.")

# Run the main function if this script is executed
if __name__ == "__main__":
    main()

