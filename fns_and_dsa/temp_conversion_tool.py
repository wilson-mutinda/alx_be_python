# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """
    Convert temperature from Fahrenheit to Celsius.
    """
    # Use the global conversion factor
    factor = FAHRENHEIT_TO_CELSIUS_FACTOR
    return (fahrenheit - 32) * factor

def convert_to_fahrenheit(celsius):
    """
    Convert temperature from Celsius to Fahrenheit.
    """
    # Use the global conversion factor
    factor = CELSIUS_TO_FAHRENHEIT_FACTOR
    return (celsius * factor) + 32

def main():
    """
    Main function to handle user interaction for temperature conversion.
    """
    print("Welcome to the Temperature Conversion Tool!")

    try:
        # Prompt the user for temperature
        temp_input = input("Enter the temperature to convert: ")
        
        # Validate numeric input
        if not temp_input.replace('.', '', 1).isdigit():
            raise ValueError("Invalid temperature. Please enter a numeric value.")
        
        temperature = float(temp_input)
        
        # Prompt the user for the temperature unit
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        
        if unit == "F":
            # Convert Fahrenheit to Celsius
            celsius = convert_to_celsius(temperature)
            print(f"{temperature}°F is {celsius:.2f}°C")
        
        elif unit == "C":
            # Convert Celsius to Fahrenheit
            fahrenheit = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {fahrenheit:.2f}°F")
        
        else:
            # Handle invalid unit input
            raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
