#print the welcome message
welcomeMessage = ("\n\t\t" + "\033[1m" + "welcome to the even odd number sorter app" + "\033[0m")
print(welcomeMessage.upper())

#get the user input inside of while loops
OddEven = True
while OddEven:
    userInput = (input("\n\tEnter in a string of numbers separated by a comma (,) : ").split(','))
    print("\n\t" + "\033[1m" + "---- Result Summary ----" +"\033[0m")
    #initializing variables
    E = []
    O = []
    #For loops inside the while loops
    for user in userInput:
        #for Even
        if (int(user) % 2) == 0:
            print (user + "\033[1m" + " is even" + "\033[0m")
            E.append(user)
        #for Odd
        else:
            print (user + "\033[1m" + " is odd" + "\033[0m")
            O.append(user)
    #Printing the results for EVEN numbers
    E.sort()
    print("\n\t" + "\033[1m" + "The following " + str(len(E)) + " are even: " + "\033[0m")
    for even in E:
        print(even)
    #Printing the results for ODD numbers
    O.sort()
    print("\n\t" + "\033[1m" + "The following " + str(len(O)) + " are odd" + "\033[0m")
    for odd in O:
        print(odd)
        #input for run again the program
    userChoice = input("\n\tWould you like to run the program again (y/n): ")
    if userChoice == 'n':
        Gmessage = ("\033[1m" + "\n\t\t" +"thank you for using the program. Goodbye." + "\033[0m")
        print (Gmessage.upper())
        break