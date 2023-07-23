a = "CSC180"
b = "CSC180"

d = "CSC"
e = "180"
f = d + e
d = 42
print(id(a), id(b), id(f))

#-5...255 are stored at fixed locations

for i in range(-10, 300):
    print(i, id(i), id(i+1)-id(i))
    
a = 19874982174319827429817432

#strings and ints are immutable
#(you cannot change their contents)

#lists *are* mutable

L1 = [1, 2, 3]
L2 = [1, 2, 3]

#id(L1) and id(L2) are different
L1 = [1, 2, 3]
L2 = L1
L2[0] = 5
L1 # [5, 2, 3]

