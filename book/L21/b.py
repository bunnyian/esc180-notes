#dictionaries

#associate keys and values
#
#
#parallel lists
kids = ["Bob", "Dorothy", "Alice"]
faves = ["candy", "costumes", "midterms"]

grades = {"PHY": 90, "CSC": 85, "CIV": 100, "ESC": 85}

grades["CSC"] = 84

grades["MAT"] = 87  #OK

L = [60, 61, 50]
#L[4] = 100 would produce an error

endowment = {2014: 180}
endowment[2015] = 200
endowment[2017] = 210

list(endowment.keys())
list(endowment.values())
list(endowment.items())

for k in grades:
    print(k)

for k in grades.keys():
    print(k)
    
for subj in grades:
    print("I got", grades[subj], "in", subj)
    
for subj, grade in grades.items():
    print("I got", grade, "in", subj)
    
for grade in grades.values():
    print("I got", grade)    
    
def get_subj_by_grade(grades, grade):
    res = []
    for subj, grade2 in grades.items():
        if grade == grade2:
            res.append(subj)
    return res
    
for grade in grades.values():
    print("I got", grade, "in", get_subj_by_grade(grades, grade))    
        
        
#keys must be immutable
d = {1:2}        
L = [4, 5]
d[L] = 50  #keys must be immutable
L[0] = 2

t  = (4, 5)
d[t] = 100

#Sparse matrices
#Matrices that mostly contain just 0s

