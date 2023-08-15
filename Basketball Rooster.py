welcomeMessage = ("\t\tWelcome to the Basketball Roster Program")
print (welcomeMessage.upper())
#get the user input
player = []
player.append(input("Who is your point guard: "))
player.append(input("Who is your shooting guard: "))
player.append(input("Who is your small forward: "))
player.append(input("Who is your power forward: "))
player.append(input("Who is your center: "))
#printing the players
print ("\n\tYour starting 5 for the upcoming basketball season")
print ("\nPoint Guard: ", player[0])
print ("\nShooting Guard: ", player[1])
print ("\nSmall Forward: ", player[2])
print ("\nPower Forward: ", player[3])
print ("\nCenter: ", player[4])
print ("\nOh no,", player[2] ,  ("is injured."))
print ("\nYour roster only has 4 players.")
#adding a new player in the list
newPlayer = input("\nWho will take "+ str(player[2])+" spot: ")
player[2] = newPlayer
#print the new player's line up
print ("\nYour starting 5 for the upcoming basketball season")
print ("\nPoint Guard: ", player[0])
print ("\nShooting Guard:", player[1])
print ("\nSmall Forward: ", player[2])
print ("\nPower Forward: ", player[3])
print ("\nCenter: ", player[4])
print ("\nGoodluck ", str(player[2]) ,  (" you will do great!"))
print ("\nYour roster now has 5 players")