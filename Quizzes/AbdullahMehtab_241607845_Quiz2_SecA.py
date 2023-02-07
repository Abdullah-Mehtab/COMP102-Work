##Quiz-2
#Task 1
print()
print("Task One")
print()
#Working
x = ("+ - + - + - + - + -")
x1 = ("- + - - - - - - - -")
x2 = ("- - - + - - - - - -")
x3 = ("- - - - - + - - - -")
x4 = ("- - - - - - - + - -")
x5 = ("- - - - - - - - - +")
#Printing
print('\n'+x+'\n'+x1+'\n'+x+'\n'+x2+'\n'+x+'\n'+x3+'\n'+x+'\n'+x4+'\n'+x+'\n'+x5)
#Using Loops 
print('\n')
a=6
for b in range(1, a):
    print("+ - " * (a - 1))
    print("- " * (2*b - 1), "+", " -" *  2 * (a - b - 1))
