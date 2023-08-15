#print the welcome message
welcomeMessage = ("\n\t\t" + "\033[1m" + "Welcome to Python Dice App" + "\033[0m")
print(welcomeMessage.upper())

# importing random on the cell
from random import randint

# creating a while loops
pyDice = True
while pyDice:
    def pyDiceApp(n, x):
        for dice in range(x):
            roll = randint(1, n)
            rolls.append(roll)
            print(roll)


    # get the user input
    numSides = int(input("\nHow many sides would you like on your dice?: "))
    numDice = int(input("\nHow many dice would you like to roll?: "))

    # printing the results
    print("\033[1m" + "\nYou rolled " + str(numDice) + " in the " + str(numSides), "sided dice." + "\033[0m")
    print("\n\t\t" + "\033[1m" + "-----Results are as followed-----" + "\033[0m")
    rolls = []
    pyDiceApp(numSides, numDice)
    print("\033[1m" + "The total value of your roll is ", sum(rolls), end="." + "\033[0m")

    # Asking a user to run the program again
    runAgain = str(input("\n\tWould you like to play again? (y/n): "))
    if runAgain.startswith('n') or runAgain == 'no':
        # if 'n', print the goodbye message
        print("\n\t\t" + "\033[1m" + "Thank you for using python dice app".upper() + "\033[0m")
        break