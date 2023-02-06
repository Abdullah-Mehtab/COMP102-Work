###Comp102 Assignment 1
##Making User friendly  
##Task one
print()
print("------------------------------")
print("Task One")
print()
#Given
print()
print("If the code is 'print(1,2,3,4)'")
print("the output is: ")
print(1,2,3,4)
print()
#Working and Printing
print("To get the needed output, we must use '\\n'.")
print('\n',1,'\n\n',2,'\n\n',3,'\n\n',4) 
print()
##Task Two
print()
print("------------------------------")
print("Task Two")
print()
#String editing
print("Converting input strings to required output strings")
print("(Look at code for working)")
#Working
print()
print("'abcd' to 'Ac'")
input1 = ("abcd")
print(input1,input1[0].upper()+input1[2])
print()
print("'9' to '57'")
input2 = ('9')
print(input2+":",ord(input2))    #ASCII value of '9' is '57'
print()
print("'PythonAssignment' to 'toA'")
input3 = ("PythonAssignment")
print(input3+":",input3[2]+input3[4]+input3[6])
print()
print("'PythonAssignment' to 'ssAnoht'")
input4 = input3[2:9]
print(input3,input4[::-1])
print()
print("'PythonAssignment' to 'Me'")
print(input3+":",input3[12].upper()+input3[13])
print()
##Task Three
print()
print("------------------------------")
print("Task Three")
print()
#To Do
print("Making a tic-tac-toe table..")
print()
#Working
Tablebody = ("+--+--+--+\n|  |  |  |")
Tablebottom = ("+--+--+--+")
#Printing
print(Tablebody)
print(Tablebody)
print(Tablebody)
print(Tablebottom)
print() 
print("Table complete!")
##Task Four
print()
print("------------------------------")
print("Task Four")
print()
#Input
Meat = int(input("Enter the amount of cicken meat: "))
Leaves = int(input("Enter the amount of lettuce leaves: "))
Tomato = int(input("Enter the amount of tomato slices: "))
#Work
MeatFix = 1
LeavesFix = 3
TomatoFix = 6
A = Meat/MeatFix
B = Leaves/LeavesFix
C = Tomato/TomatoFix
Burger = min(A,B,C)
#Print
print()
print("Burger: ",Burger)
print()
##Task Five
print()
print("------------------------------")
print("Task Five")
print()
#To do
print("Removing white spaces.")
#Work
pif = ("                            Programming is fun :-)")
print()
print(pif)
print()
#Print
print(pif.strip()) #Using the strip method
print()
##Task Six
print()
print("------------------------------")
print("Task Six")
print()
#To do
print("Milarity time format into hours and minutes")
#Input
t1 = int(input("Enter the first time: "))
t2 = int(input("Enter the second time: "))
#Working
tdiff = t2 - t1
hours = tdiff // 100
mins = tdiff % 100
hours = hours + mins // 60
mins = mins % 60
#Print
print()
print("Converting..")
print()
print(hours,"hours",mins,"minutes")
print()
input("Press any key to end.")