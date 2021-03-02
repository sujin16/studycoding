def solution(arr):
    table =[0]*len(arr)
    table[0] =1
    cur = arr[0]
    for i in range(1,len(arr)):
        if cur>arr[i]: table[i]=table[i-1]+1
        else: table[i] =table[i-1]
        cur= arr[i]
    return len(arr) - table[-1]

arr=[2,7,5,2]
print(solution(arr))
