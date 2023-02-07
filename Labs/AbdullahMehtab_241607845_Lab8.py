###Lab Eight
print()
print("Lab Eight")
print()
##Task One
print()
print("-"*20)
print("Task One")
print()
#Working
list1 = [1,1,2,2,3,3,4,4,5,5,6]
def evenhello(t1list):
      for x in range(len(t1list)):
           if t1list[x]%2==0:
                t1list[x]="hello"
      return t1list
#printing
print(list1)
print()
print(evenhello(list1))
##Task Two
print("\n")
print("-"*20)
print("Task Two")
print()
#Working
list2 = [1,2,3,4,5,6,7,8,9,10]
def reverselist(t2listx):
     reversedlist = t2listx[::-1]
     return reversedlist
#printing
print(list2)
print('reversing...')
print(reverselist(list2))
##Task Three
print('\n')
print("-"*20)
print('Task Three')
print()
#Working
list3 = []
print("Empty list: \n",list3,"\n")
list3 = list(range(1, 21))
print("Natural numbers list: \n",list3)
##Task Four
print("\n")
print("-"*20)
print("Task Four")
print()
#Working
from random import randint
list4 = []
for i in range(10):
     list4.append(randint(1,100))
print("List of ten random distinct numbers between 1 and 100:")
print(list4)
##Task Five
print("\n")
print("-"*20)
print("Task Five")
print()
#Working
list5 = [2,4,8,16]
print(list5)    
result = 1
for x in list5:
     result = result * x
print("Multiplying..")
print(result)
print('\n')
input("Press ENTER to end")
