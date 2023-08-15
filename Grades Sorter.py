#Get the welcome message
welcomeMessage = ("\t\tWelcome to Grade Sorter App")
print (welcomeMessage.upper())
#get the user input
grade1 = int(input("\nWhat is your First Grade (0 - 100): "))
grade2 = int(input("\nWhat is your Second Grade (0 - 100): "))
grade3 = int(input("\nWhat is your Third Grade (0 - 100): "))
grade4 = int(input("\nWhat is your Fourth Grade (0 - 100): "))
gradeList = []
gradeList.append(grade1)
gradeList.append(grade2)
gradeList.append(grade3)
gradeList.append(grade4)
#print all the grades
print ("\nYour grades are: ", gradeList)
gradeSorted = sorted(gradeList, reverse =True)
print ("\nYour grades from highest to lowest are: ", gradeSorted)
lowestGrade=[]
lowestGrade.append(gradeSorted[2])
lowestGrade.append(gradeSorted[3])
#removing the two lowest grades
print ("\nThe lowest two grades will now be dropped.")
print ("\nRemoved grade: ", lowestGrade[1])
print ("\nRemoved grade: ", lowestGrade[0])
gradeSorted.pop()
gradeSorted.pop()
print ("\nYour remaining grades are: ", gradeSorted)
print ("\nNice work! Your highest grade is a", gradeSorted[0])