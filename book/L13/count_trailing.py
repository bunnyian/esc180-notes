def fact(n):
    res = 1
    for i in range(1, n):
        res *= i
    return res
    
    

def count_trailing_A(n):
    count5 = 0
    for i in range(1, n):
        while i % 5 == 0:
            count5 += 1
            i //= 5
    return count5
            
def count_trailing_B(n):
    res = 0
    fact_n = fact(n)
    while fact_n % 10 == 0:
        res += 1
        fact_n //= 10
    
    return res
    
    
count_trailing_A(100000)
count_trailing_B(100000)
    