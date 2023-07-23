#Merge Sort

#[10, 2, 4, 20, 3]

def merge(L1, L2):
    i, j = 0, 0
    merged = []
    #L1[:i] was already processed
    #L2[:j] was already processed
    
    while i < len(L1) and j < len(L2):
        if L1[i] < L2[j]:
            merged.append(L1[i])
            i += 1
        else:
            merged.append(L2[j])
            j += 1
    
    merged.extend(L1[i:])
    merged.extend(L2[j:])
    
    return merged

def merge_sort(L):
    '''Returns the sorted version of L'''
    if len(L) <= 1:
        return L[:]
    
    mid = len(L)//2
    return merge(merge_sort(L[:mid]), merge_sort(L[mid:]))