#Encrypting password input.
import getpass

#Display welcome message.
welcomeMessage = ("\033[1m" + "\n\t\twelcome to the database admin program." + "\033[0m")
print (welcomeMessage.upper())

#Create a dictionary to hold all username:password key-value pairs
log_on_information = {
    'admin':'admin',
    'nirvana':'cobain',
    'metallica':'hetfield',
    'slipknot':'taylor',
    'beatles':'mccartney',
    }
#Login account banner
print("\033[1m" + "\nLogin Account" + "\033[0m")

#Get user input
username = input("USERNAME: ")

#Simulate logging in...
#Get user password
if username in log_on_information.keys():
    password = getpass.getpass("PASSWORD: ")
    if password == log_on_information[username]:
        print("\nHello " + "\033[1m" + username + "\033[0m" + "! You are successfuly logged in!")
        if username == 'admin':
            #Show the whole database to the admin account
            print("\033[1m" + "\nHere is the current user database:" + "\033[0m")
            print("")
            for key, value in log_on_information.items():
                print("\033[1m" + "\tUsername: " + "\033[0m" + key + "\033[1m" + "\t\tPassword: " + "\033[0m" + value)
        else:
            #Allow standard user to change their password
            password_change = input("\nWould you like to change your password? (yes/no): ").lower().strip()
            if password_change == 'yes':
                new_password = getpass.getpass("What would you like your new password to be? (Minimum of 8 characters): ")
                if len(new_password) >= 8:
                    log_on_information[username] = new_password
                    print("\033[1m" + "\nPassword Changed!" + "\033[0m")
                else:
                    print("\033[1m" + "\nMESSAGE!" + "\033[0m")
                    print(new_password + " is not the minimum eight characters.")
                    print("\033[1m" + "\nMESSAGE!" + "\033[0m")
                    print("Please login again and change your password (Minimum of 8 characters).")
                print("\n***********************************************************************************************")
                print("\033[1m" + "\nACCOUNT DETAILS: " + "\033[0m")
                print("\033[1m" + username + "\033[0m" + ", your password now is " + "\033[1m" + log_on_information[username] + "\033[0m" + ".")
            else:
                print("\033[1m" + "\nMESSAGE!" + "\033[0m")
                print("The password did not change. Thank you.")

    #User did not enter their password correctly
    else:
        print("\033[1m" + "\nMESSAGE!" + "\033[0m")
        print("Password incorrect! Please login again.")

#User not in database
else:
    print("\033[1m" + "\nMESSAGE!" + "\033[0m")
    print("Username is not in the database!")
