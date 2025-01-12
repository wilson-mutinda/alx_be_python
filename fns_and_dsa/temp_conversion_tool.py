FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
  """Converts a temperature from Fahrenheit to Celsius.

  Args:
      fahrenheit: The temperature in Fahrenheit.

  Returns:
      The temperature converted to Celsius.
  """
  return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
  """Converts a temperature from Celsius to Fahrenheit.

  Args:
      celsius: The temperature in Celsius.

  Returns:
      The temperature converted to Fahrenheit.
  """
  return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

# ... (rest of the code remains the same as in the previous response)

def main():
  """Prompts the user for temperature input and performs conversion."""
  while True:
    try:
      temperature = float(input("Enter the temperature to convert: "))
      unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

      if unit not in ("C", "F"):
        raise ValueError("Invalid unit. Please enter 'C' or 'F'.")

      if unit == "C":
        converted_temp = convert_to_fahrenheit(temperature)
        unit_label = "°C"
      else:
        converted_temp = convert_to_celsius(temperature)
        unit_label = "°F"

      print(f"{temperature:.1f}{unit_label} is {converted_temp:.2f}°F" if unit == "C" else f"{temperature:.1f}{unit_label} is {converted_temp:.2f}°C")
      break
    except ValueError as e:
      print(f"Error: {e}")

if __name__ == "__main__":
  main()
