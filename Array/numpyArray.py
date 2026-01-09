from numpy import *

val = array([1,2,3,4,5])

for x in val:
    print(x, end = " ")
    
arr = array([1,2,3.2,True,"Hello"])

print("\n")
for x in arr:
    print(x, end= " ")
    
print("\n")

#Arithmetic Progression

#linspace

arr2 = linspace(10,20,50)

for i in arr2:
    print(i, end=" ")
    
print("\n")
#arange
arr3 = arange(10,20,2)

for j in arr3:
    print(j, end=" ")
    
#Multi dimensional array

#zero dimensional array
zero = array(10)
print(zero)

#One Dimensional array
one = array([1,2,3,4,5])
print(one)

#Two Dimensional array

two = array([[1,2,3],[4,5,6]])
print(two)

#Three Dimensional array
three = array([
    [[1,2,3],
     [4,5,6]],
    
    [[7,8,9],
     [10,11,12]]
    
    ])
print(three)