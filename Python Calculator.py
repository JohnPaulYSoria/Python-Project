# print the welcome message
welcomeMessage = ("\n\t\tWelcome to the Python Calculator App")
print(welcomeMessage.upper())
print("Enter two numbers and an operation and the desired operation will be performed")
CalSummary = []


# get the user input
def pyCalculator():
    num1 = float(input("\nEnter a number: "))
    num2 = float(input("Enter a number: "))
    userChoice = str(
        input("Enter an operation  (addition, subraction, multiplication, division, or exponentiation): ")).lower()

    # for ADDITION
    if userChoice == 'addition' or userChoice == 'a':
        addition = num1 + num2
        print("\033[1m" + "The sum of " + str(num1) + " and " + str(num2) + " is " + str(addition) + "\033[0m")
        CalSummary.append("{} + {} = {}".format(num1, num2, addition))
    # for SUBTRACTION
    elif userChoice == 'subtraction' or userChoice == 's':
        subtraction = num1 - num2
        print(
            "\033[1m" + "The difference of " + str(num1) + " and " + str(num2) + " is " + str(subtraction) + "\033[0m")
        CalSummary.append("{} - {} = {}".format(num1, num2, subtraction))
    # for MULTIPLICATION
    elif userChoice == 'multiplication' or userChoice == 'm':
        multiplication = num1 * num2
        print(
            "\033[1m" + "The product of " + str(num1) + " and " + str(num2) + " is " + str(multiplication) + "\033[0m")
        CalSummary.append("{} * {} = {}".format(num1, num2, multiplication))
    # for DIVISION
    elif userChoice == 'division' or userChoice == 'd':
        if num2 == 0:
            print("\033[1m" + "You cannot divide by zero!" + "\033[0m")
            CalSummary.append('DIV ERROR')
        else:
            division = num1 / num2
            print("\033[1m" + "The qoutient of " + str(num1) + " and " + str(num2) + " is " + str(division) + "\033[0m")
            CalSummary.append("{} / {} = {}".format(num1, num2, division))
    # for EXPONENTIATION
    elif userChoice == 'exponentiation' or userChoice == 'e':
        exponentiation = num1 ** num2
        print("\033[1m" + "The result of " + str(num1) + " raised to the " + str(num2) + " power is " + str(
            exponentiation) + "\033[0m")
        CalSummary.append("{} ** {} = {}".format(num1, num2, exponentiation))
    else:
        print("\033[1m" + "That's not a valid operator. Try Again." + "\033[0m")
        CalSummary.append('OPP ERROR')
    CalStats()

    # for user if wants to run the program again


def CalStats():
    runAgain = str(input("Would you like to run the program again? (y/n): "))
    if runAgain == 'y':
        pyCalculator()
    # displaying the CALCULATION SUMMARY
    elif runAgain == 'n':
        print("\033[1m" + "\nCalculation Summary:" + "\033[0m")
        for results in CalSummary:
            print(results)
        # goodbye message
        print("\033[1m" + "\n\t\t" + "thank you for using python calculator app. goodbye!".title())
    else:
        CalStats()


pyCalculator()