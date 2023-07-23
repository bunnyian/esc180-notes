def mult_M_v(M, Mdim, v):
    res = [0]*Mdim[0]
    
    
    #coords: (1, 2) -->
    #    multiply M[(1, 2)]*v[2] and 
    #             place the result in 
    #              res[1]
    for coords in M.keys():
        res[coords[0]] += M[coords]*v[coords[1]]




M = {(1, 2): 3, (4, 5):2}
v = [4, 3, 10, 2, 12, -5, 6]
Mdim = (7, 7)

M = 0 0 0 0 0 0 0     4         0
    0 0 3 0 0 0 0     3        30  
    0 0 0 0 0 0 0    10        0
    0 0 0 0 0 0 0     2        0
    0 0 0 0 0 2 0    12        -10
    0 0 0 0 0 0 0    -5        0
    0 1 0 0 0 0 0     6        3