def solution(m,n,puddles):
    dist =[[1]*(m) for i in range(n)]
    
    for i in range(m-1):
        if [0,i] in puddles: puddles.append([0,i+1])
    for i in range(n-1):
        if [i,0] in puddles: puddles.append([i+1,0])
    
    for i in range(1,n):
        for j in range(1,m):
            if [i+1,j+1] in puddles:continue
            else:
                if [i,j+1] in puddles and [i+1,j] in puddles : puddles.append[i,j]
                else:
                    a = dist[i-1][j] if [i,j+1] not in puddles else 0
                    b = dist[i][j-1] if [i+1,j] not in puddles else 0
                    dist[i][j] =a+b
                    if [i,j] ==[n-1,m-1]: return dist[i][j]

print(solution(	4, 3, [[2, 2]]))