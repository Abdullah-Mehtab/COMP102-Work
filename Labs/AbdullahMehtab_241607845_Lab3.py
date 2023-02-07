###Lab 3
##Task 1
print()
print("Task One")
print()
#Input
Gallons = input("Write the number of gallons of gas in the tank: ")
Eff = input("Write the fuel efficiency in miles/gallon: ")
Price = input("Write the price of gas: ")
#Work
G = int(Gallons)
E = int(Eff)
P = int(Price)
Miles = (100/E)*P
Dist = G*E
#Print
print()
print("Cost per 100 miles: ",Miles)
print("Distance Car can go with gas in tank: ",Dist)
print()
##Task Two
print()
print("Task Two")
print()
print("I've used two different methods to do this task since I couldn't figure out strip-concatenation method")
print("My method also displays error if wrong input is entered")
#Work
print()
print("-------------------------")
print("Method One")
print()
months = ['January', 'Feburary', 'March', 'April', 'May', 'June', 'July', 
              'August', 'September', 'October', 'November', 'December']
try:
    mon = int(input('Enter the number to be converted into a month: '))
    if mon < 1 or mon > 12:
        raise ValueError
    else:
        print("Month: ",months[mon - 1])
except ValueError:
    print("Invalid number, please input from 1-12.")
print()
print("-------------------------")
print("Method Two")
print()
numb = int(input("Enter the number  number: "))
Months="  January  February     March     April       May      June      July    August September   October  November  December"

if numb==1:
    print("Month: ",Months[0:numb*12-1].strip())
else:
    print("Month: ",Months[(numb-1)*10:numb*10].strip())
print()
print("Lab 3: Complete")
input("Press any Key to end.")