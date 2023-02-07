##Quiz Three
print()
print("Quiz Three")
print()
#Working
def sum_of_numbers(n):
     if (n > 0 and n < 10):
         total = 0
         while (n > 0 and n < 10):
             print(str(n)+"+",end="")
             total += n 
             n -= 1
         return total
     else:
         print("Please input a positive number under 10")
print("0 =",sum_of_numbers(5)) #Input the required value here (replace 5)
#Complete
input("\nPress ENTER to end.")