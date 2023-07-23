L = [1, 2, 3]
L1 = L #L1 and L are aliases

##################################

L1 = [L[0], L[1], L[2]]

L1 = L[:] #shorthand for [L[0], ..., L[-1]]

L1 = []
for e in L:
    L1.append(e)
    
###################################    

#L[0] = 5 doesn't modify L1[0] and vice versa

L = [[1, 2], [3, 4]]
L1 = L[:]  #[L[0], L[1]]

L[0] = 5
L[1][0] = 7 #same as L1[1][0]

L = [[1, 2], [3, 4]]
L1 = [[L[0][0], L[0][1]], [L[1][0], L[1][1]]]