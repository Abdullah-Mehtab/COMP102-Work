##Lab 12
print()
print("Lab 12")
print()
##Task One
print()
print("Task One")
print()
#Working
natural = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("First Ten natural numbers:", natural)
print("\nFilfering even numbers: ",list(filter(lambda x: x % 2 == 0, natural)))
print("\nFiltering odd numbers: ",list(filter(lambda x: x % 2 != 0, natural)))
##Task Two
print('\n')
print("Task Two")
print()
#Working
print("First Ten natural numbers:",natural)
print(natural)
print("\nMapping even numbers:",list(map(lambda x: x % 2 == 0, natural)))
print("\nMapping odd numbers:",list(map(lambda x: x % 2 != 0, natural)))
##Task Three
print('\n')
print("Task Three")
print()
#Working
a = [1,2,3,5,7,9]
b = [2,3,5,6,7,8]
print('a =',a)
print('b =',b)
print("\nCommon numbers in 'a' and 'b':",list(filter(lambda x: x in b, a))) #Filter Lambda method
##Task Four
print('\n')
print("Task Four")
print()
#Working
a = [1,2,3,5,7,9]
b = [2,3,5,6,7,8]
print('a =',a)
print('b =',b)
print("\nCommon numbers in 'a' and 'b':",list(x for x in a if x in b)) #List comprehension method


