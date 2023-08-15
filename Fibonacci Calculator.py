#print the welcome message
welcomeMessage = ("Welcome to the Fibonacci Calculator App")
print(welcomeMessage.upper())
#get the user input
fibonacci = int(input("How many digits of the Fibonacci Sequence would you like to compute: "))
#simplifying variables
x = 0
y = 1
a = 0
c = 1
#looping for fibonacci
for i in range(1,fibonacci+1):
    print(y)
    z=x+y
    x=y
    y=z
print ( )
#looping for Golden Ratio
print ("The corresponding Golden Ratio values are: ")
print ( )
fibonaccilist = [0,1]
for i in range(0,fibonacci):
    fibonaccilist.append(fibonaccilist[i] + fibonaccilist[i+1])
gratio=[fibonaccilist[i] / float(fibonaccilist[i-1]) for i in range(2,len(fibonaccilist))]
for i in gratio :
    print (i)
print ( )
print("The ratio of consecutive Fibonacci terms approaches Phi; 1.618...")