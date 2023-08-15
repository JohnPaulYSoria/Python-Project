# print the welcome message
welcomeMessage = ("\033[1m" + "Welcome to the Prime Number App" + "\033[0m")
print(welcomeMessage.upper())

# print the instructions
Prime = True
while Prime:
    print("\nEnter 1 to determine if a specific number is prime.")
    print("Enter 2 to determine all prime numbers within a set range.")

    # get the choice of user input
    userChoice = int(input("\n\tEnter your choice 1 or 2: "))
    # for specific prime number
    while userChoice == 1:
        Num = int(input("\nEnter a number to determine if it is prime or not: "))

        # formula for prime number
        if Num > 1:
            for i in range(2, Num):
                if (Num % i) == 0:
                    print("\t\t" + str(Num) + "\033[1m" + " is not prime!" + "\033[0m")
                    break
            else:
                print("\t\t" + str(Num) + "\033[1m" + " is a prime!" + "\033[0m")
                break
        break

    # for prime number within a set in range
    while userChoice == 2:

        # get the user input
        numOne = int(input("\nEnter the lower bound of your range:"))
        numTwo = int(input("Enter the upper bound of your range: "))
        print("\nCalculations took a total of 0.0 seconds.")
        print("\n\t\t" + "\033[1m" + "The following numbers between", numOne, "and", numTwo, "are prime:" + "\033[0m")
        input("Press enter to continue.")

        # formula for prime number within a set in range
        for numbers in range(numOne, numTwo + 1):
            if numbers > 1:
                for i in range(2, numbers):
                    if (numbers % i) == 0:
                        break
                else:
                    print(numbers)
        break
    while userChoice != 2 and userChoice != 1:
        print("\nThat is not a valid option.")
        break

    # get the user input for starts the program again
    runAgain = input("\nWould you like to run the program again (yes/no): ")
    if runAgain.startswith("y"):
        print(userChoice)
    else:
        prime = True
        # if the user type 'no' or 'n' in runAgain input, print the goodbye message
        print("\n\tThank you for using the program. Have a nice day.".upper())
        break