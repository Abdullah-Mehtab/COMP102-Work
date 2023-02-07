###Lab Four
print()
print("Lab Five")
print()
##Task One
print()
print("------------------------------")
print("Task One")
print()
#Working
i = 1
j = 1
for i in range(1,11):
       for j in range(1,11):
             print("",i*j, end="")           
       print()
##Task 2
print()
print("------------------------------")
print("Task Two")
print()
#Working
x = 1
while x < 21: 
       print ('2^'+str(x), '=' ,'\t', 2**x)
       x += 1
##Task 3
print()
print("------------------------------")
print("Task Three")
print()
#Working
num = input("Please enter the number: ")
odd_sum = 0
for sub in num:
    for ele in str(sub): 
        if int(ele) % 2 == 0:
            break
        else:
            odd_sum += int(ele)
#Printing
print("Odd digit sum: " + str(odd_sum))
##Task 4
print()
print("------------------------------")
print("Task Four")
print()
#Working
number = 8
print('I have a number between 1 and 20.\n')
guessesTaken = 0
while guessesTaken < 5:
     print('\nTake a guess.')
     guess = input()
     guess = int(guess)
     guessesTaken += 1

     if guess != number:
             print('Your guess is wrong!')
     if guess == number:
         break
#Printing
if guess == number:
     guessesTaken = str(guessesTaken)
     print("\nCongratulations!, you guessed my number in " + guessesTaken + " guesses!")

if guess != number:
     number = str(number)
     print('\nNope. The number I was thinking of was ' + number)
#Lab5 complete
input("\nPress ENTER to end.")


            
          
      

