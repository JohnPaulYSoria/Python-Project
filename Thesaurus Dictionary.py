#Importing random.
import random

#Thesaurus words inside of dictionary
thesaurus = {
    'cute':['charming','delightful','adorable','pretty'],
    'ugly':['unbeautiful','awful','uncomely','horrid'],
    'shy':['humble','afraid','cautious','fearful'],
    'should':['will','be going to','shall','must'],
    'win':['succeed','conquer','prevail','triumph'],
    'perfect':['excellent','ideal','pure','splendid'],
    'enemy':['antagonist','opponent','adversary','foe'],
    'private':['secret','intimate','individual','confidential']
}

#print the welcome message
welcomeMessage = ("\033[1m" + "\n\t\twelcome to the thesaurus app!" + "\033[0m")
print(welcomeMessage.upper())

#Display welcome information.
print("\nChoose a word from the thesaurus and I will give you a synonym.")
print("\nHere are the words in the thesaurus: ")

for key in thesaurus.keys():
    print("\t"+ key)

#Get user input.
choice = input("\nPlease choose a word above: ").lower().strip()

#Provide a random synonym.
if choice in thesaurus.keys():
    index = random.randint(0,4)
    print("\nA synonym for " + choice + " is " + "\033[1m" +  thesaurus[choice][index] + "\033[0m" + ".")
else:
    print("I'm sorry, that word is not currently in the thesaurus.")

#Get user input to see the whole thesaurus.
choice = input("\nWould you like to see the whole thesaurus? (yes/no): ").lower().strip()

#Show all values in the thesaurus
if choice == 'yes':
    for key, values in thesaurus.items():
        print("\n" + "\033[1m" + key.title() + " synonyms are: " + "\033[0m" )
        for value in values:
            print("\t" + value)
else:
    print("\n\t\tI hope you enjoyed the program. Thank you!".upper())
