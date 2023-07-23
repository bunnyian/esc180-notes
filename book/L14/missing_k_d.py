#1...n, k is missing, find k

#[1, 5, 2, 4]  -> [1, 2, 4, 5]

#[1, 2, 3, 4, 5] -> [2, 3, 4, 5]
#[1, 2, 3, 4, 5] -> [1, 2, 3, 4]

#[1, 2, 3, 4]

def missing_k_D(L):
    sorted_L = sorted(L) #L.sort()
    
    n = len(sorted_L) + 1
    
    if sorted_L[0] != 1:
        return 1
        
    if sorted_L[-1] != n:
        return n
    
    for i in range(0, len(sorted_L)-1):
        if sorted_L[i+1] - sorted_L[i] == 2:
            return sorted_L[i] + 1
    
    
    
    
print(missing_k_D([1, 5, 2, 4]))