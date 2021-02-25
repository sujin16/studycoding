from itertools import combinations
def comb(lst,n):
    ret =[]
    if n>len(lst):return ret
    if n ==1:
        for i in lst: ret.append([i])
    elif n>1:
        for i in range(len(lst)-n+1):
            for temp in comb(lst[i+1:],n-1): ret.append([lst[i]+temp])
    return ret
def check(arr):
    if len(arr)<2 or len(arr)%2!=0: return False
    num = max(arr,key=arr.count)
    
    if arr.count(num)*2 !=len(arr):return False
    
    for i in range(0,len(arr)-1,2):
        if arr[i] ==arr[i+1]:return False
    return True
def solution(a):
    size= len(a) 
    if size%2==0 or size<2:return 0
    num=2
    arr =list(set(combinations(a,num)))
    while num<=size:
        for 
    return 0

print(solution(		[1, 2, 2, 1, 3]))

a =set([(1,2),(1,2)])
print(list(a))