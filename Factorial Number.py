import math
#print the welcome message
welcomeMessage = ("Welcome to the Factorial Calculator App")
print(welcomeMessage.upper())

#get the user input
num1=int(input("What number would you like to compute the factorial of? "))

#getting the fibonacci formula and result
print(str(num1) + "!= ", end=" ")
for i in range (1,num1):
    print (str(i), end= "*")
fact=1
for i in range (1,num1+1):
    fact=fact*i
print(num1)
print()
print("The factorial of ", num1, " is", fact)