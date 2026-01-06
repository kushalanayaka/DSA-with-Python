# import array as arr
from array import *

val = array('i', [1,2,3,4,5]) #typecode - i, d, u
# val = array('u', ['a', 'p', 'p'])

for i in range(0, len(val)): #len()
    print(val[i], end=" ")

print("\n")

for x in val:
    print(x, end=", ")

print("\n")
val.reverse()
for x in val:
    print(x, end=", ")

print("\n")
print(val.typecode)

#*****************************************************************

val.insert(1, 100)
val.append(1000)

# print("\n")
val[5] = 500
for i in val:
    print(i, end=" ")

cpy_arr = array(val.typecode, (x*2 for x in val))
print("\n")
# for i in cpy_arr:
#     print(i, end=" ")

#*****************************************************************

cpy_arr.pop(0)
cpy_arr.remove(1000)
for i in cpy_arr:
    print(i, end=" ")

#*****************************************************************
# sclicing
print("\n")
sli = cpy_arr[2 : 6]
for i in sli:
    print(i, end=" ")

