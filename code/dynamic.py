def solution(a):
    table=[0]*100
    table[0] =a[0]
    table[1] =max(a[0],a[1])
    for i  in range(2,len(a)):
        table[i] = max(table[i-2]+a[i], table[i-1])
    return table[-1]
    
arr= [1,3,1,5]
print(solution(arr))

