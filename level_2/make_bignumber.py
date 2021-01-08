from itertools import combinations

def solution(number,K):
    numbers= set(combinations(number,len(number)-K))
    arr =[int("".join(x)) for x in numbers]
    return str(max(arr))
   

number='1231234'
K=3
print(solution(number,K))



