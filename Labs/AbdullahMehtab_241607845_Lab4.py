###Lab Four
print()
print("Lab Four")
print("\n")
##Task One
print()
print("Task One")
print()
#Working
def favmovie(defmovie = "Spider-Man-Homecoming"):    
     usermovie = input("Please enter your favorite movie : ")  
     if usermovie is (""):
      print("\nYour favorite movie is " + defmovie) 
     if usermovie is not (""):
      print("\nYour favorite movie is " + usermovie)
      
#print
favmovie()
print()
##Task Two
print()
print("Task Two")
print()
#Working
def caluculator():
      x = int(input('First Integer: '))
      y = int(input('Second Integer: '))     
      sum = x + y
      diff = x - y
      product = x*y
      div = x/y
      print("\n Sum: ",sum,"\n","Difference: ",diff,"\n","Product: ",product,"\n","Division: ",div)
      return
def sum(x,y):
      return x + y 
def diff(x,y):
      return x - y
def product(x,y):
      return x * y
def div(x,y):
      return x / y
#print
caluculator()
print()
##Task Three
print()
print("Task Three")
print()
#Working
def Repeat():
      rep = input("Write any string: ")
      reping = ("\n"+rep)
      print("Printing 20 times..")
      print(reping*20)
print()
#Print
Repeat()
print()
##Task Four
print()
print("Task Four")
print()
#Working
taskfourstr = input("Write any English sentence:\n")
print()
def splitting():
      splittedstr = taskfourstr.split()
      print('Splitted String: ')
      print(splittedstr)
      return
def counting():
      countingstr = taskfourstr.count('e')
      print('Counting number of "e": ')
      print(countingstr)
      return
#Print
splitting()
print()
counting()
print('\n')
##Complete
print("Lab Four Complete")
input("Enter anything to end")

     