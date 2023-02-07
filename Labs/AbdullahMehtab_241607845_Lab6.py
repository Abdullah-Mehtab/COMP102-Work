###Lab Six
print()
print("Lab Six")
print()
##Task One
print()
print("------------------------------")
print("Task One")
print()
#Working
n = int(input("Enter an integer assigning the length for the diamond: \n"))
print()
for a in range(1, 2 * n):
    if a <= n: 
            ndots = 2 * a - 1
    elif a > n: 
        ndots = (2 * n - a) * 2 - 1
    nspaces = (2 * n - 1 - ndots) // 2
    print(" " * nspaces, end = "")
    print("*" * ndots, end = "")
    print(" " * nspaces)
print()
##Task Two
print()
print("--------------------------------")
print("Task Two")
print()
#Working
from random import randint 
x = 0 
y = 0
for i in range(100):
    direction = randint(1, 4)
    if direction == 1:
        x = x - 1
    elif direction == 2:
        x = x + 1
    elif direction == 3:
        y = y + 1
    else:
        y = y - 1
#Printing
print("(" + str(x) + ", " + str(y) + ")")
print()
#Task Three
print()
print("--------------------------------")
print("Task Three")
print()
#Working
word = input("Please enter any word: ")
print()
for i in range(1, len(word) + 1):
    for pos in range(0, len(word) - i + 1):
        print(word[pos : pos + i])
print()
#Lab 6 Complete
input("Press ENTER to end.")