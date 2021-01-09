from itertools import combinations
from math import comb
def solution(clothes):
    closet ={}
    for i in range(len(clothes)):
        key = clothes[i][1] 
        if key not in closet: closet[key] =0;closet[key]+=1
        else: closet[key]+=1
    answer =[]
    for val in closet.values():
        answer.append(val)
    result =0
    answer_len =len(answer)
    if answer_len ==len(clothes):
        return sum([comb(answer_len,i)for i in range(1,answer_len+1)])

    for i in range(1,len(answer)+1):
        arr= list(combinations(answer,i))
        for a in arr:
            num =1       
            for b in a: num*=b
            result+=num
    
    print(result)
    return result


clothes= [["yellow_hat","headgear"],
["blue_sunglasses","eyewear"],
["green_turban","headgear"]]

print(solution(clothes))