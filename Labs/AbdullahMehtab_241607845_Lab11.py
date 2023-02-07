##Lab 11
print()
print("Lab 11")
print()
##Task One
print()
print("Task One")
print()
#Working
def sum_of_list(inputlist):
      a = len(inputlist)
      if a == 1:
           return inputlist[0]
      else:
           return inputlist[0] + sum_of_list(inputlist[1:])
#Printing
list1 = [1,2,3,4,5]
print(list1)
print("\nSum of numbers in list: \n")
print(sum_of_list(list1))
##Task Two
print("\n")
print("Task Two")
print()
#Working
def a_power_b(a, b):
	if a == 0:
		return 0
	elif b == 0:
		return 1
	elif b == 1:
		return a
	else:
		return a * a_power_b(a, b - 1)
base = int(input("Please enter the base (a): "))
power = int(input("Please enter the power of the base (b): "))
#Printing
print("\nCalculating...")
print(a_power_b(base,power))
##Task Three
print("\n")
print("Task Three")
print()
#Working
def checkLucky(num):
    if num > 0:
        if num % 10 == 8:
            return True
        if checkLucky(num//10): #This checks the unwinding condition
                return True
    else:
        return False


t3numb = int(input("Please enter a number to check if its lucky or not: "))
#Printing
if checkLucky(t3numb) == True:
      print("\nYour number '"+str(t3numb)+"' is lucky!")
else:
      print("\nYour number '"+str(t3numb)+"' isn't lucky.")
#Task Four
print("\n")
print("Task Four")
print()
#Working
def strreversing(inputstr):
      x = len(inputstr)
      if x == 0:
           return inputstr
      else:
           return strreversing(inputstr[1:]) + inputstr[0] 

inputstr = input("Please enter a string to reverse: ")
print()
print("Reversed string: \n" + strreversing(inputstr))
#Complete

input("\nPress Enter to END")