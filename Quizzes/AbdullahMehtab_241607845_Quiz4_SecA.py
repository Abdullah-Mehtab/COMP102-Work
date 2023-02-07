##Quiz Four
#Your name: Abdullah Nehtab 
#Your Roll Number: 241607845
print()
print("Quiz Four")
print()
# Please write code to access and print 'apple' present in every list.
#1
a=['apple', 'orange', 'banana','mango']
#your code
print(a[0])
print()
#2
b=['orange', ['apple'], 'banana','mango']
#your code
b1 = b[1]
print(b1[0])
print()
#3
c=['orange', [['apple']], 'banana','mango']
#your code
c1 = c[1]
c2 = c1[0]
print(c2[0])
print()
#4
d=['orange', (2, 'apple'), 'banana','mango']
#your code
d1 = d[1]
print(d1[1])
print()
#5
e=['orange', [(6,7, ['apple'])], 'banana','mango']
#your code
e1 = e[1]
e2 = e1[0]
e3 = e2[2]
print(e3[0])
print()
#6
f=[[[[[['apple']]]]]]
#your code
f1 = f[0]
f2 = f1[0]
f3 = f2[0]
f4 = f3[0]
f5 = f4[0]
print(f5[0])
print()
print("COMPLETE!")