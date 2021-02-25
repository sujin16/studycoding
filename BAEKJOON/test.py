def knapsack(capacity,n):
    arr =[[0 for _ in range(capacity+2)] for _ in range(n+2)]
    for i in range(1,n+1):
        for s in range(1,capacity+1):
            if size[i-1]>s:
                arr[i][s] =arr[i-1][s]
            else:
                arr[i][s] =max(val[i-1]+arr[i-1][s-size[i-1]],arr[i-1][s])
    return arr[n][capacity]

n,k = map(int,input().split())
size,val =[],[]
for _ in range(n):
    a,b =map(int,input().split())
    size.append(a)
    val.append(b)

print(knapsack(k,n))