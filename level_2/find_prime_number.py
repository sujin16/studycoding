from itertools import permutations
from math import sqrt
def check_prime(n):
    k = sqrt(n)
    if n<2: return False
    
    for i in range(2,int(k)+1):
        if n%i ==0: return False
    return True
            

def soultion(n):
    answer =[]
    for i in range(1,len(n)+1):
        perlist = list(map(''.join,permutations(list(n),i)))
        for j in list(set(perlist)):
            if check_prime(int(j)):
                answer.append(int(j))
    return len(set(answer))

n ='011' 
soultion(n)