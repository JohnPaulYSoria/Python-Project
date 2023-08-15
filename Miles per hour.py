#print the welcome message\n",
welcomeMessage = ("Welcome to Miles Per Hour Conversion App")
print(welcomeMessage.upper())
#get the user input
number = float(input("What is your speed in Miles Per Hour: "))
#formula for taking the meters per second\n",
Conversion_Factor = 0.4474
s = 60
m = 1
Miles = round(number * Conversion_Factor, 2)
#results of the speed in meters per second\n",
print ("Your speed in meters per second is: " + str(Miles))