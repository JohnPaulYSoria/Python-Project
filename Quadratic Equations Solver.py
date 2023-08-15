import cmath

#print the welcome message
welcomeMessage = ("\t\tWelcome to Quadratic Equation Solver App.")
print(welcomeMessage.upper())

#printing meaning of quadratic equation
print("A quadratic equation is of the form ax^2 + bx + c = 0")
print("Your solution can be real or complex numbers.")
print("A complex number has two parts: a + bj")
print("Where a is the real portion and bj is the imaginary portion.")

#get the user input for equations would like to solve
num1 = int(input("\n\tHow many equations would you like to solve today: "))
eq1 = list(range(1,num1))

#main loop and formulas
for i in range(1, num1+1):
    print("\t\tSolving equation number:",i)
    #get the user input
    a=float(input("Please enter your value of a (coeffiecient of x^2): "))
    b=float(input("Please enter your value of b (coeffiecient of x): "))
    c=float(input("Please enter your value of c (coeffiecient): "))
    print("\nThe solutions to " + str(a) + "x^2 + " + str(b) + "x + " + str(c) + " = 0 are:")
    #formula to get the answers
    d = (b**2)-(4*a*c)
    x1 = (-b-cmath.sqrt((b**2)-(4*a*c)))/(2*a)
    x2 = (-b+cmath.sqrt((b**2)-(4*a*c)))/(2*a)
    print("\nx1 = " + str(x1))
    print("\nx2 = " + str(x2))
print("\n\t\tThank you for using the Quadratic Equation Solver App. Goodbye.")