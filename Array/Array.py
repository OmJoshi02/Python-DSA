#import array module

from array import *

#integer array
integer = array('i', [1,2,3,4])
# print(integer)

#character array
char = array('u', ['a','b','c','d','e','f'])
# print(char)

#Size of array
print("size of array : ",len(integer))

print()


#copy array

copyArray = array(integer.typecode, (x*2 for x in integer))
print("This is copyArray : ",copyArray)
#Normal for loop
print("Integer array")
print("typecode : ", integer.typecode)
for i in range(0, len(integer)):
    print(integer[i], end= ", ")
    
print("\n")

print("Character array")
print("typecode : ", char.typecode)
for i in range(0, len(char)):
    print(char[i], end= ", ")
    
print("\n")

#Enhanced for loop
print("Enhanced for loops")
for x in integer:
    print(x, end= ", ")

print()

for x in char:
    print(x, end=", ")
    

print("\n")
#Reverse the array

integer.reverse()

for i in integer:
    print(i, end= ", ")
    

print("\n")


#Insert element
integer.insert(1,50)
for i in integer:
    print(i, end= ", ")
    
print("\n")
#Insert element at last
integer.append(100)
for i in integer:
    print(i, end= ", ")
    
print("\n")


#pop
integer.pop()
for i in integer:
    print(i, end= ", ")
    

#Remove
integer.remove(100)
for i in integer:
    print(i, end= ", ")