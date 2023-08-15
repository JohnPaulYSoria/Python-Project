#Encrypting password input.
import getpass

#Display welcome message.
welcomeMessage = ("\033[1m" + "\n\t\tWELCOME TO THE YES or No ISSUE POLLING APP" + "\033[0m")
print(welcomeMessage.upper())

#Get user input
issue = input("\nWhat is the yes or no issue you will be voting on today?: ")
vote_number = int(input("What is the number of voters you will allow on the issue?: "))
password =  getpass.getpass("Enter a password for the polling results: ")

#Initialize our variables
yes = 0
no = 0
results = {}

#Simulate voting
for i in range(vote_number):
    name = input("\nEnter your full name: ").title().strip()
    if name in results.keys():
        print("Sorry, it seems that someone with that name has already voted.")
    else:
        print("Here is our issue: " + issue)
        choice = input("What do you think? yes or no?: ").lower().strip()
        if choice == 'yes' or choice == 'y':
            choice = 'yes'
            yes += 1
        elif choice == 'no' or choice == 'n':
            choice = 'no'
            no += 1
        else:
            print("That is not a yes or no answer, but okay...")
        #Add vote to the dictionary results
        results[name] = choice
        print("\033[1m" +"MESSAGE: " + "\033[0m" + "Thank you " + name + "!  Your vote of " + results[name] + " has been recorded.")

#Show who actually voted
total_votes = len(results.keys())
print("\033[1m" + "\nThe following " + str(total_votes) + " people voted: " + "\033[0m")
for key in results.keys():
    print(key)

#Summarize the voting results
print("\033[1m" + "\nOn the following issue: "+"\033[0m"  + issue)
if yes > no:
    print("Yes wins! " + str(yes) + " votes to " + str(no) + ".")
elif no > yes:
    print("No wins! " + str(no) + " votes to " + str(yes) + ".")
else:
    print("It was a tie! " + str(no) + " votes to " + str(yes) + ".")

#Allow the admin to see the actual votes
guess =  getpass.getpass("\nTo see the voting results enter the admin password: ")
if guess == password:
    for key, value in results.items():
        print("\033[1m" +"\tVoter: " +"\033[0m" + key + "\033[1m" + "\t\t\tVote: " + "\033[0m" + value)
else:
    print("Sorry, that is not the correct password.  Goodbye...")

print("\n\033[1m" + "\n\t\tMESSAGE: " + "\033[0m" + "Thank you for using the Yes or No Issue Polling App.")
