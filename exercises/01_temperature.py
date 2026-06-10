'''Temperature converter
Converts temperatures from Celsius to Fahrenheit and vice versa based on user input.
Validates the input, in case the user types somethign that's not a number by printing an appropriate message instead of crashing.
'''

def convert_temperature():
    print("***** Temperature Converter *****")

    user_input_temperature =input("Enter the temperature value: ")
    try:
        temperature = float(user_input_temperature)
    except ValueError:
        print("Error! Please enter a valid number (e.g. 44 or 16.12).")
        return
    
    unit = input("Value in Celsius or Fahrenheit? (C/F):").upper()

    if unit =="C":
        converted = (temperature *9/5)+32
        print(temperature, "°C is equal to",round(converted, 2), "°F.")
    elif unit == "F":
        converted = (temperature - 32)*5/9
        print(temperature, "°F is equal to",round(converted, 2), "°C.")
    else:
        print("Error! Invalid unit! Please enter 'C' or 'F'")

if __name__ =="__main__":
    convert_temperature()