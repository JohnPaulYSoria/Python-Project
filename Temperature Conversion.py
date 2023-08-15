#print the welcome message
welcomeMessage = ("Welcome to the Temperature Conversion App")
print (welcomeMessage.upper())
#get the user input,
Fahrenheit = float(input("What is the given temperature in degrees Fahrenheit: "))
#formulas for taking the Celsius and Kelvin
Celsius = ((Fahrenheit - 32.0) * (5.0/9.0))
Kelvin = 273.5 + ((Fahrenheit - 32.0) * (5.0/9.0))
#Printing the results
print ("Degrees Fahrenheit: ", Fahrenheit)
print ("Degrees Celsius: " + str(format(Celsius, '.4f')))
print ("Degrees Kelvin: " + str(format(Kelvin, '.4f')))
