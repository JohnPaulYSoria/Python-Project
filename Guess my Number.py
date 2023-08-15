import random

#Print the welcome message
welcomeMessage = ("\t\tWelcome to the Guess My Number App")
print(welcomeMessage.upper())
print()

#Get user input
guessesTaken = 0
print('Hello! What is your name?')
name = input()

#Pick a random integer from 1 to 20
number = random.randint(1, 20)
print("Well, " + name + ", I am thinking of a number between 1 and 20.")

#Guess the number 5 times
while guessesTaken < 5:
   print("\nTake a guess.") 
   guess = input() 
   guess = int(guess)
   guessesTaken = guessesTaken + 1

#Conditions if the guessing number is too low or too high
   if guess < number:
     print("Your guess is too low.") 

   elif guess > number:  
    print("Your guess is too high.")
   
#The game is done, recap winning or loosing
if guess == number:
    guessesTaken = str(guessesTaken)
    print("\nGood job, "  + name + "! You guessed my number in " + guessesTaken + " guesses!")

else:
    number = str(number)
    print("\nGame Over. The number I was thinking of was " + number + ".")