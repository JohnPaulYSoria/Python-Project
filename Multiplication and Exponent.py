import math
#print the welcome message
welcomeMessage = ("\t\tWelcome to the Multiplication/Exponent Table Program")
print (welcomeMessage.upper())
#get the user input
Name = input("\nHello, what is your name: ")
Num = float(input("\n\nWhat number would you like to work with: "))
#printing the multiplication and exponent table
print ("\t\tMultiplication Table for", Num)
for i in range (1,10):
       print (i,'x',Num,'=',round(Num*i,2))
print ("\t\tExponent Table of: ", Num)
for i in range (1,10):
       print (Num, '**',i, '=', round(Num**i,4))