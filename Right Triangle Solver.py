import math
#print the welcome message
welcomeMessage = ("\t\tWelcome To Right Triangle Solver App")
print (welcomeMessage.upper())
print ()
#get the user input\n",
Firstleg = float(input("\nWhat is the First Leg of the Triangle: "))
Secondleg = float(input("\nWhat is the Second Leg of the Triangle: "))
#getting the formulas
hypotenuse = math.sqrt(Firstleg**2 + Secondleg**2)
area = (1/2)*(Firstleg*Secondleg)
#print the results
print("\nFor  triangle with legs of ",  str(Firstleg), "and ", str(Secondleg), "the hypotenuse is ", str(round(hypotenuse, 3)))
print("\nFor triangle with legs of ", str(Firstleg), "and ", str(Secondleg), "the area is ", str(round(area, 3)))