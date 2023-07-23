from numpy import *


def print_matrix(M):
    print("The matrix is currently:")
    print(array(M))
    print("="*80)

def get_lead_ind(arr):
    for i in range(len(arr)):
        if arr[i] != 0:
            return i
    return len(arr)

def get_row_to_swap(M, start_i):
    best_lead_ind = len(M[0])
    best_i = len(M[0]) 
    for i in range(start_i, len(M)):
        lead_ind = get_lead_ind(M[i])
        if lead_ind < best_lead_ind:
            best_i = i
            best_lead_ind = lead_ind
    return best_i, best_lead_ind
    

def subtract_rows_coefs(r1, c1, r2, c2):
    r = [0]*len(r1)
    for i in range(len(r1)):
        r[i] = c1*r1[i]-c2*r2[i]
    return r
    
def subtract_rows(M, row_to_sub, best_lead_ind):
    for row1 in range(row_to_sub+1, len(M)):
        if M[row1][best_lead_ind] != 0:
            M[row1] = subtract_rows_coefs(M[row1], 1, 
                                            M[row_to_sub], M[row1][best_lead_ind]/M[row_to_sub][best_lead_ind] )
            #M[row1][best_lead_ind] = 0 #Making sure! If we don't do this, there 
                                       #will be a lot of trouble

def div_lead_coef(r):
    i = get_lead_ind(r)
    if i < len(r):
        ri = r[i]
        for j in range(i, len(r)):
            r[j] /= ri



def forward_step(M):
    for row in range(len(M)):
        print("Now looking at row %d" % (row))
        best_i, best_lead_ind = get_row_to_swap(M, row)
        if best_i == len(M[0]):
            break
        print("Swapping rows %d and %d so that entry %d in the current row is non-zero" % (row, best_i, best_lead_ind))
        M[row], M[best_i] = M[best_i], M[row]
        
        print_matrix(M)
        
        print("Adding row %d to rows below it to eliminate coefficients in column %d" % (row, best_lead_ind))
        
        subtract_rows(M, row, best_lead_ind)
        
        print_matrix(M)

    
    


def subtract_rows_back(M, row_to_sub, best_lead_ind):
    for row1 in range(row_to_sub):
        if M[row1][best_lead_ind] != 0:
            M[row1] = subtract_rows_coefs(M[row1], 1, 
                                            M[row_to_sub], M[row1][best_lead_ind]/M[row_to_sub][best_lead_ind] )

def backward_step(M):
    for row in range(len(M)-1, -1, -1):
        lead_ind = get_lead_ind(M[row])
        
        print("Adding row %d to rows above it to eliminate coefficients in column %d" % (row, lead_ind))
        subtract_rows_back(M, row, lead_ind)
        
        print_matrix(M)
        
    
        



##set b to the basis vectors
def solve(M, b):
    aug = []
    for i in range(len(M)):
        aug.append(M[i]+[b[i]])
        
    print_matrix(aug)
    
    
    print("Now performing the forward step")
    forward_step(aug)
    
    print_matrix(aug)
    
    print("Now performing the backward step")
    backward_step(aug)
    
    print("Now dividing each row by the leading coefficient")
    for i in range(len(aug)):
        div_lead_coef(aug[i])
        
    print_matrix(aug)
    
    x = []
    for i in range(len(aug)):
        x.append(aug[i][-1])
    return x
    

#from numpy import *
#from copy import deepcopy

#M = array([[1,-2,3],[3,10,1],[1,5,3]])
#x = array([75,10,-11])
#b = dot(M,x)        

#b = [1, 0, 0]
#b = [0, 1, 0]
#b = [0, 0, 1]

#print("x =", solve(M.tolist(), b.tolist()))


################################################################################

#Build a Hilbert matrix

n = 3
M = zeros((n, n)) #[[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]]
for i in range(n):
    for j in range(n):
        M[i][j] = 1/(i+j+1) 
#M = array([[1,-2,3],[3,10,1],[1,5,3]])
        
x = array([75,10,-11])
#x = array([1,0,0])
b = dot(M,x)      
#b = array([0, 0, 1])

print("x =", solve(M.tolist(), b.tolist())) #incorrect solution due to ill-conditioning
    
#Mx1 = [1, 0, 0]^T    
    
#Trying to solve Mx=b by first finding M^-1
#Problem: change M just a little bit => M^-1 changes by a lot
#       slight imprecision in the intermediate steps will propagate
x = 0.00000001  +0.001
1/x


  