# Global conversion factors
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9

def convert_to_celsius(fahrenheit):
    """Converts Fahrenheit to Celsius using the global conversion factor."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit using the global conversion factor."""
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

def main():
    try:
        # Prompt the user for a temperature value
        temperature_input = float(input("Enter the temperature to convert: "))  # Prompt must match exactly

        # Prompt for the unit, and handle case-sensitivity
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        # Conversion logic
        if unit == 'C':
            converted_temp = convert_to_fahrenheit(temperature_input)
            print(f"{temperature_input}°C is {converted_temp}°F")
        elif unit == 'F':
            converted_temp = convert_to_celsius(temperature_input)
            print(f"{temperature_input}°F is {converted_temp}°C")
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")  # Ensure this matches exactly

if __name__ == "__main__":
    main()

