#tuples

a = (42, 43, 100)



#tuple unpacking
a = (42, 43, 100)
i, j, k = a

a = 42
b = 43
a, b = b, a #(b, a)

def f():
    return 42, 43
    
a, b = f()    

c = f()
a = c[0]
b = c[1]
