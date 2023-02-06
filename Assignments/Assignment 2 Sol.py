###Assignment Two
print()
print("Assignment two")
##Task 1
print()
print("------------------------------")
print("Task one")
print()
#Working
T1word1 = input("Please enter the first word: ")
T1word2 = input("Please enter the second word: ")
print()
ttl = 50
ttl = 50 - len(T1word1) + len(T1word2)
def FiftyChrLine(T1w1, T1w2):
     """
     This function prints two words 
     The frst word left-justified
     The second word right-justified
     With periods in between to complettere 50 characters
     """
     print(T1w1, T1w2, sep=ttl*".")
#Printing
print("Result: ")
print()
FiftyChrLine(T1word1, T1word2)
##Task 2
print()
print("------------------------------")
print("Task two")
print()
#Working
T2word1 = input("Please enter first word: ")
T2word2 = input("Please enter second word: ")
print()
def compareword(T2w1, T2w2):
     """
     This function compares two words
     It compares if the first word is bigger than the second word
     """
     if len(T2w1) > len(T2w2):
        return True
     else:
        return False
#Checking and Printing
check = compareword(T2word1, T2word2)
if check==True:
     print("The frst word is longer than the second word.")
else:
     print("The frst word is not longer than the second word.")
print()
##Task 3
print()
print("------------------------------")
print("Task three")
print()
#Working
T3sentence = "Miss Umber has no mercy marking her quiz."
T3word = "mercy"
def container(T3S1, T3W):
     """
     This function checks if the given word is in the sentence
     OR not
     """
     print("Checking if word is in sentence.\n")
     if T3word in T3sentence:
         print("True")
     else:
         print("False")
#Printing
container(T3sentence, T3word)
print()
##Task 4
print()
print("------------------------------")
print("Task four")
print()
#Working
Alphabet = input("Enter any alphabet Aa-Zz: ")
print()
def alphabettype(letter):
     """
     This function prompts an alphabet from the user
     Then it checks if its a vowel or a consonant and tells the user
     """ 
     if letter=="a" or letter=="A" or letter=="e" or letter=="E" or letter=="i" or letter=="I" or letter=="o" or letter=="O" or letter=="u" or letter=="U":
        print("It is a vowel.")
     elif letter=="b" or letter=="c" or letter=="d" or letter=="f" or letter=="g" or letter=="h" or letter=="j" or letter=="k" or letter=="l" or letter=="m" or letter=="n" or letter=="p" or letter=="q" or letter=="r" or letter=="s" or letter=="t" or letter=="v" or letter=="w" or letter=="x" or letter=="y" or letter=="z":
        print("It is a consonant.")
     elif letter=="B" or letter=="C" or letter or letter=="D" or letter=="F" or letter=="G" or letter=="H" or letter=="J" or letter=="K" or letter=="L" or letter=="M" or letter=="N" or letter=="P" or letter=="Q" or letter=="R" or letter=="S" or letter=="T" or letter=="V" or letter=="W" or letter=="X" or letter=="Y" or letter=="Z":
        print("It is a consonant.")
#Printing    
if len(Alphabet) > 1 or Alphabet.isdigit():
     print("Error404")
else:
     alphabettype(Alphabet)
##Task 5
print()
print("------------------------------")
print("Task Five")
print()
#Working
number = int(input("Enter number between 1 and 4000:\n"))
roman = ""
I = 1
IV = 4
V = 5 
IX = 9
X = 10
L = 50
XC = 90
C = 100
D = 500
CM = 900
M = 1000
print()
x = number
romandone = False
while romandone == False:
    while x >= M:
        if x >= M:
            x = x - M
            roman = roman + "M"
    while x >= CM:
        if x >= CM:
            x = x - CM
            roman = roman + "CM"
    while x >= D:
        if x >= D:
            x = x - D
            roman = roman + "D"
    while x >= C:
        if x >= C:
            x = x - C
            roman = roman + "C"
    while x >= XC:
        if x >= XC:
            x = x - XC
            roman = roman + "XC"
    while x >= L:
        if x >= L:
            x = x - L
            roman = roman + "L"
    while x >= X:
        if x >= X:
            x = x - X
            roman = roman + "X"
    while x >= IX:
        if x >= IX:
            x = x - IX
            roman = roman + "IX"
    while x >= V:
        if x >= V:
            x = x - V
            roman = roman + "V"
    while x >= IV:
        if x >= IV:
            x = x - IV
            roman = roman + "IV"
    while x >= I:
        if x >= I:
            x = x - I
            roman = roman +"I"

        
    if x==0:
       romandone = True
    
print("The roman numeral for the given number is: ")
print(roman)
print()
##Task Six
print()
print("------------------------------")
print("Task Six")
print()
#Working
from random import randint
T6Word = input("Please enter a word: ")
for i in range(len(T6Word)):    
    rand_i = randint(0, len(T6Word) - 2)
    rand_j = randint(rand_i + 1, len(T6Word) -1)
    first = T6Word[: rand_i]
    i = T6Word[rand_i]
    middle = T6Word[rand_i + 1 : rand_j]
    j = T6Word[rand_j]
    last = T6Word[rand_j + 1 :]
    T6Word = first + j + middle + i + last
#Printing
print()
print(T6Word)
##Task Seven
print()
print("------------------------------")
print("Task Seven")
print()
#Working
T7numb = int(input("Enter an integer: "))
print()
for i in range(1, T7numb + 1):
    for j in range(1, 2 * T7numb + 1):
        if j == T7numb + 1: 
            print(" *", end = "")
        elif T7numb + 1 < j < 2 * T7numb and 1 < i < T7numb:
            print(" ", end = "")
        elif j == 2 * T7numb:
            print("*")     
        else:
            print("*", end = "")
print()
#Task Eight
print()
print("------------------------------")
print("Task Eight")
print()
#Working
cardnum = input("Enter a valid card number: ")
pos = len(cardnum) - 1
sum1 = 0 
sum2 = 0 
while pos >= 0:
     if pos % 2 == 1:
        sum1 = sum1 + int(cardnum[pos])
     else:
        num = int(cardnum[pos])
        num = 2 * num 
        for digit in str(num):
            sum2 = sum2 + int(digit)
     pos = pos - 1
print()
#Printing
if (sum1 + sum2) % 10 == 0:
    print("Card number is valid.\n")
else: 
    print("Card number is invalid.\n")
    sumWithoutCheck = sum1 - int(cardnum[len(cardnum) - 1])
    validCheckDigit = 10 - ((sumWithoutCheck + sum2) % 10)
    
    print("The check digit " + str(validCheckDigit) + " would make it valid.")
print()
##Task Nine
print()
print("------------------------------")
print("Task Nine")
print()
#Working
T9numb = int(input("Please enter an integer: "))
print()
firstprime = 2 
for firstprime in range(2, T9numb + 1):
    prime = True
    for i in range(2, firstprime):
        if firstprime % i == 0:
            prime = False
    if prime == True:
        print(firstprime)
print()
##Assignment Two complete
input("Press ENTER to end.")