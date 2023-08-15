import math
#print the welcome message
welcomeMessage = ("\t\tWelcome to the Average Calculator App ")
print (welcomeMessage.upper())
#get the user input
totgrades = []
totgrades.sort(reverse = False)
name = input("\nWhat is your name: ")
subNo = int(input("\nHow many grades would you like to enter: "))
#looping a grade summary
for i in range(subNo):
    totgrades.append(int(input("Enter Grade: ")))
avg = sum(totgrades) / len(totgrades)
#printing the grades hiighes to lowest
print("Grades Highest to Lowest: ")
for s in sorted(totgrades,reverse = True):
    print(s)
print ((name) +"'s", "New Grade Summary:")
print ("Total number of Grades:", (subNo))
print ("Highest Grade: ", max(totgrades))
print ("Lowest Grade: ", min(totgrades))
print ("Average: ", avg)
#getting the desired average grades\n",
Davg = int(input("\nWhat is your desired average: "))
D = int(len(totgrades)+1)
get = D*Davg - sum(totgrades)
print("\nGoodluck", name,"!")
print("\nYou will need to get a", round(get,1),"on your next assignment to earn a", round(Davg,1),"average.")
print("\nLets see what your average could have been if you did better worse on an assignment.")
copy = totgrades.copy()
copy.sort(reverse = True)
#getting the grade would like to change
new = int(input("\nWhat grade would you like to change: "))
new1 = int(input("\nWhat grade would you like to change "+ str(new)+" to: "))

#looping a new grade summary
if new in copy:
    copy[copy.index(new)] = new1
print("\nNew Grades Highest to Lowest: ")
for c in sorted(copy,reverse = True):
    print(c)
avg1 = sum(copy) / len(copy)
#printing the new results
print ((name) +"'s", "New Grade Summary:")
print ("Total number of Grades:", (subNo))
print ("Highest Grade: ", max(copy))
print ("Lowest Grade: ", min(copy))
print ("Average: ", avg1)
print("\nYour new average would be a ", avg1," compared to your real average of ", avg,"!")
change = avg1 - avg
print("\nThat is a change of ", change, " points!")
print()
print("\nToo bad your original grades are still the same! ")
print(sorted(totgrades,reverse =True))
print("\nYou should go ask for extra credit!")