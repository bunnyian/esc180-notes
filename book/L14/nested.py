#counter will contain the number of times that print
#has run so far
#(also, the order of the current print operation)
counter = 0
for i in range(5):
    
    #do:
    ###########
    for j in range(3):
        counter += 1
        print(counter,": i = ", i, ", j = ", j)
        #counter += 1 
    ###########
    #for i = 0, 1, 2, 3, 4
    
#total number of times the inner for-block runs:
#5*3 = 15  


def count_i(i, n_times):
    global counter
    for j in range(n_times):
        counter += 1
        print(counter,": i = ", i, ", j = ", j)


counter = 0
for i in range(5):
    count_i(i, 3)
    
    
# print all the possible passwords that use
# the letters ["a", "b", "c", "d", "e", "f"]    
      
alphabet =  ["a", "b", "c", "d", "e", "f"]    
for letter1 in alphabet:
    for letter2 in alphabet:
        for letter3 in alphabet:
            for letter4 in alphabet:
                for letter5 in alphabet:
                    print(letter1+letter2+letter3+letter4+letter5)     
                    
def are_all_different(square):
    L = []
    for i in range(3):
        for j in range(3):
            L.append(square[i][j])
    #look for gaps of 0 in sorted(L)


#square = [[2, 9, 4],
#          [1, 5, 6], 
#          [7, 8, 3]]
          