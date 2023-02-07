##Task One
print()
print("Task One")
print()
#String
quote1 = "Courage was what it takes to stand up and speak; courage was also what it takes to sit down and listen."
#Replace
quote2 = quote1.replace("was", "is")
#Print
print
print(quote1)
print(quote2)
print()
##Task Two
print()
print("Task Two")
print()
#Arithmetic
x = int(input('First Integer: '))
y = int(input('Second Integer: '))
#Work
sum = x + y
diff = x - y
product = x*y
avg = (x+y)/2
maximum = max(x,y)
minimum = min(x,y)
#Print
print()
print("Sum: ",sum,"\n","Difference: ",diff,"\n","Product: ",product,"\n","Average: ",avg,"\n","Max: ",maximum,"\n","Minimum: ",minimum)
print()
##Task Three
print()
print("Task Three")
print()
#Input
driveletter = input('Enter drive letter: ')
thepath = input('Enter path: ')
filename = input('Enter file name: ') 
extension = input('Enter file extension: ')
#Print
completepath = (driveletter+":\\"+thepath+"\\"+filename+"."+extension)
print()
print("Complete path:",completepath)
print()
##Task Four
print()
print("Task Four")
print()
#Large Letters
LETTER_H = "*   *\n*   *\n*****\n*   *\n*   *\n"
LETTER_E = "*****\n*\n*****\n*\n*****\n"
LETTER_L = "*\n*\n*\n*\n*****\n"
LETTER_O = "*****\n*   *\n*   *\n*   *\n*****\n"
#Print
print("A Big 'Hello' using 'n' ")
print()
print(LETTER_H)
print(LETTER_E)
print(LETTER_L)
print(LETTER_L)
print(LETTER_O)
print()
##Task Five
print()
print("Task Five")
print()
#Input
evenword = input("Even length string: ")
oddword = input("Odd length string: ")
#Work
evenlength = int(len(evenword))
oddlength = int(len(oddword))
evenfirst = evenword[0]
evenmid1 = evenword[int(evenlength/2)]
evenmid2 = evenword[int(evenlength/2-1)]
evenlast = evenword[int(evenlength-1)]
oddfirst = oddword[0]
oddmid = oddword[int((oddlength-1)/2+1)]
oddlast = oddword[int(oddlength-1)]
#Print
print()
print("For Even string")
print("First Character: ", evenfirst)
print("Middle Character: ", evenmid2+evenmid1)
print("Last Character: ", evenlast)
print()
print("For Odd string")
print("First Character: ", oddfirst)
print("Middle Character: ", oddmid)
print("Last Character: ", oddlast)
print()
##Task Six
print()
print("Task Six")
print()
#Input
numbersix = input("Write a number between 1,000 and 999,999 and add a comma in the input: ")
#Work
newnumbersix = numbersix.replace(',', '')
#Print
print()
print("Result: ",newnumbersix)
print()
##Task Seven
print()
print("Task Seven")
print()
#Input
Reverse1 = input("Write a random string to reverse: ")
#Work
def my_function(x):
  return x[::-1]
Reversed1 = my_function(Reverse1)
#Print
print("Reversed output: ",Reversed1)
print()
##Task Eight
print()
print("Task Eight")
print()
#Input
a = input("Write any number to swap: ")
b = input("Write another number to swap: ")
print("A: ", a)
print("B: ", b)
#Work
c = a
d = b
b = c
a = d
#Print
print()
print("Swapped Variables")
print("A: ",a)
print("B: ",b)
print()
##Task Nine
print()
print("Task Nine")
print()
#Input
Side1 = input("Give length of one side of the rectangle: ")
Side2 = input("Give length of the other side of the rectangle: ")
#Work
Area = int(Side1)*int(Side2)
Perimeter = 2*(int(Side1)+int(Side2))
#Print
print()
print("Area of the rectangle: ",Area)
print("Prerimeter of the rectangle: ",Perimeter)
print()
##Task Ten
print()
print("Task Ten")
print()
#Input
Repeater = input("Write any string: ")
#Work
Repeating = ("\n"+Repeater)

print()
print("Printing 20 times..")
print(Repeating*20)
print()
#Complete
print()
print("Congratulations! Lab-2 Assignment complete!")
print("")
#Extra
rows = int(input("Enter any number for a diamond(the higher the number, bigger the dimond): "))   
k = 2 * rows - 2  
for i in range(0, rows):  
    for j in range(0, k):  
        print(end=" ")        
    k = k - 1        
    for j in range(0, i + 1):  
        print("* ", end="")  
    print("")      
k = rows - 2    
for i in range(rows, -1, -1):  
    for j in range(k, 0, -1):  
        print(end=" ")   
    k = k + 1   
    for j in range(0, i + 1):  
        print("* ", end="")  
    print("")  
print()
print()