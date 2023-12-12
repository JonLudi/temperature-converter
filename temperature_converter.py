print("Welcome to Temperature Converter, a lightweight utility for converting temperature.")

#Create variable for the unit that's being converted and the temperature
unit = input ("Please specify the temperature you want converted: ").upper()
value = float(input("Please specify the temperature you want converted: "))

#Function that converts C to f
def c_to_f(temp_c):
    converted_c = temp_c * (9/5) + 32
    return converted_c
#Function that converts F to C
def f_to_c(temp_f):
    converted_f = (temp_f -32) * (5/9)
    return converted_f
#Function that converts F to K
def f_to_k(temp_f):
    converted_f = (temp_f +459.67) * (5/9)
    return converted_f
def k_to_f(temp_k):
    converted_k = (temp_k -273.15) * (9/5)
    return converted_k
def c_to_k(temp_c):
    converted_c = (temp_c -273.15)
    return converted_c
def k_to_c(temp_k):
    converted_k = (temp_k +273.15)
    return converted_k
#Main Function that uses conditionals to decide which convert function to select
def main():
    if(unit =="C"):
        celsius_to_Fahrenheit = c_to_f(value)
        return celsius_to_Fahrenheit
    elif(unit =="C"):
        celsius_to_kelvin = c_to_k(value)
        return celsius_to_kelvin
    elif(unit == "F"):
        fahrenheit_to_celsius = f_to_c(value)
        return fahrenheit_to_celsius
    elif(unit == "F"):
        fahrenheit_to_kelvin = f_to_k(value)
        return fahrenheit_to_kelvin
    elif(unit == "K"):
        kelvin_to_fehrenheit = f_to_k(value)
        return kelvin_to_fehrenheit
    elif(unit == "K"):
        kelvin_to_celsius = k_to_c(value)
        return kelvin_to_celsius
else:
warning = "Please enter C or F to specify the unit:"
return warning 

#Print results
result = main()
print("Your value is:" + str(result))