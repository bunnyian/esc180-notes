L1 = [1, 2]
L2 = [4, 5]

L = L1 + L2 #compute [1, 2, 4, 5], place it in memory

L1 = L1 + L2

L1.extend([3, 4]) #id(L1) stays the same

def add_lists_bad(L1, L2):
    L1 = L1 + L2
    
def add_lists_good(L1, L2):
    L1.extend(L2)
    #L1 += L2 is the same as L1.extend(L2)
    
    
    