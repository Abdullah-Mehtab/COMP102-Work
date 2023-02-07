##Lab 10
from typing import Dict


print()
print("Lab 10")
print()
##Task One
#a)	Write a code line that converts a float no into an integer.
print("A)\n")
a = 1.0
print(a)
print(type(a))
print("\nConverting\n")
a = int(a)
print(a)
print(type(a))
#b)	Write a code line that converts any number into a String.
print("\nB)\n")
b = 12345
print(b)
print(type(b))
print("\nConverting\n")
b = str(b)
print(b)
print(type(b))
#c)	What will be the answer to the expression 2+2*2 in python?
print("\nC)\n")
c = 2+2*2
print("2 + 2 * 2 = ",c)
##Task Two
print('\n')
print("Task Two")
print()
#Working
nat = int(input("Please input any natural number: "))
print("Multiplying by 20..")
print(nat * 20)
##Task Three
print('\n')
print("Task Two")
print()
#Working
speed = 12
distance = 377.2
Gfuel = int(input("Please enter the amount of fuel in GALLONS: "))
Lfuel = Gfuel*3.79
distancecovered = Lfuel * speed
print("\nTotal distance covered by car",distancecovered)
if distancecovered < distance:
     distanceleft = distance - distancecovered
     print("The amount of distance left is",distanceleft)
else:
     distanceextra = distancecovered - distance
     print("The amount of extra distanced covered is", distanceextra)
##Task Four
print('\n')
print("Task Four")
print()
#Working
def amplifier(x,y):
     z = str(x * y)
     print(z+"Hz")
freq = int(input("Please enter the frequency: "))
no_of_times = int(input("Please enter time number of times it needs to be amplified: "))
print()
amplifier(freq,no_of_times)
##Task Five
print('\n')
print("Task Five")
print()
#Working
age1 = int(input("\nEnter age of 1st person: "))
age2 = int(input("\nEnter age of 2st person: "))
age3 = int(input("\nEnter age of 3st person: "))
age4 = int(input("\nEnter age of 4st person: "))
age5 = int(input("\nEnter age of 5st person: "))
def check(age1,age2,age3,age4,age5):
	 teenage = []
	 if age1 < 19 and age1 > 10:
		 teenage.append(age1)
	 if age2 < 19 and age2 > 10:
		 teenage.append(age2)
	 if age3 < 19 and age3 > 10:
		 teenage.append(age3)
	 if age4 < 19 and age4 > 10:
		 teenage.append(age4)
	 if age5 < 19 and age5 > 10:
		 teenage.append(age5)
	 return teenage

print("\nThe ages of teenages in the given ages: ")
print(check(age1,age2,age3,age4,age5))
##Task Six
print('\n')
print("Task Six")
print()
#Working
word = input("Please enter any word: ")
print()
for i in range(1, len(word)+1):
     for pos in range(0, len(word)-i+1):
         print(word[pos:pos+i])
##Task Seven
print('\n')
print("Task Seven")
print()
#Working
print("See the attached image")
##Task Eight
print('\n')
print("Task Eight")
print()
#Working
natural = [1,2,3,4,5,6,7,8,9,10]
print("Set 1",natural)
even = [2,4,6,8,10,12,14,16,18,20]
print("Set 2",even)
def intersect(x,y):
     intersection = set.intersection(set(x), set(y))
     intlist = list(intersection)
     return intlist
print("Intersecting Set 1 and 2...")
print(intersect(natural,even))
##Task Nine
print('\n')
print("Task Nine")
print()
#Working
Dictionary = {
         "Emp1" : {'Name' : 'Amir', 'ID' : 101 , 'Department' : 'Printing' , 'Salary' : 2500},
         "Emp2" : {'Name' : 'Laura', 'ID' : 123 , 'Department' : 'Typewriting' , 'Salary' :5000},
         "Emp3" : {'Name' : 'Zain', 'ID' : 134, 'Department' : 'Posting', 'Salary': 2000},
         "Emp4" : {'Name' : 'Safdar', 'ID' : 169, 'Department' : 'Managing', 'Salary': 7500}}

print(Dictionary)
print()
e1d = Dictionary['Emp1']
e1 = e1d['Salary']
e2d = Dictionary['Emp2']
e2 = e2d['Salary']
e3d = Dictionary['Emp3']
e3 = e3d['Salary']
e4d = Dictionary['Emp4']
e4 = e4d['Salary']

emplist = [e1,e2,e3,e4]

def max(Dictonary):
      l = emplist[0]
      for num in emplist:
           if num> l:
                l = num
      return l

def min(Dictionary):
      s = emplist[0]
      for num in emplist:
           if num< s:
                s = num
      return s

print('Minimum Value: ', min(Dictionary))
print('Maximum Value: ', max(Dictionary))

#Complete

input("\nPress Enter to END")