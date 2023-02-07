###Lab 9
print()
print("Lab 9")
print()
#Task 1
print()
print("Task One")
print()
#Working
dict1 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
chk = int(input("Enter any integer key: "))
if chk in dict1:
     print('\nKey is present in the dictionary')
else:
     print('\nKey is not present in the dictionary\n Adding key to dictionary')
     dict1.update({chk:chk*10})
     print("Updated dictionary:\n",dict1)
print
#Task 2
print()
print("Task Two")
print()
#Working 
dict2_1 = {'Computer' : 'PC', 'Programming' : 'Coding', 'Maths': 'Arithmetic', 'Statistics' : 'Probability'}  
dict2_2 = {'Electronics' : 'Circuits', 'Battery' : 'Voltage', 'Current' : 'Ampere', 'Resistance' : 'Conductance'}  
print(dict2_1)
print()
print(dict2_2)
dict2_1.update(dict2_2)   
print("\nMerging the two dictionaries: \n")  
print(dict2_1) 
print()
#Task 3
print()
print("Task Three")
print()
#working
n=int(input("Input the highest number for the dictionary: "))
dict3 = {}
for x in range(1,n+1):
    dict3[x]=x*x
print()
print(dict3)
print()
#Task 4
print()
print("Task Four")
print()
#Working
dict4 = {1:'a', 2:'b', 3:'c', 4:'d'}              
print(dict4)
print()
print('List of given keys and their values:\n')
for key, value in dict4.items():
    print(key, ":", value)
print()
#Complete
input("Press ENTER to End")
