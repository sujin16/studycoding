n,m = map(int,input().split())
INF  =float('inf')
graph = [[INF]*(n+1) for _ in range(n+1)]
for i in range(1,n+1): graph[i][i] =0
for i in range(m):
    a,b = map(int, input().split())
    graph[a][b] =1
    graph[b][a] =1
    
x,k = map(int,input().split())

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j] =min(graph[i][j], graph[i][k]+graph[k][j])

count=0
val = distance[1][k] + distance[k][x]
if val!=INF: print(val)
else: print(-1)
