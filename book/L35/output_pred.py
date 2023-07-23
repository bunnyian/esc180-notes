L = [[5, 6], [7, 8]]
M = L[:][:]
M[0][1] = "I am altering the list"
M[1] = "Pray I don't alter it any further"
print(L)