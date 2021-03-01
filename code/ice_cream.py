def dfs(x,y):
    if (x<0 or x>n or y<0 or y>n): return False
    if graph[x][y] ==0:
        graph[x][y] =1
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y+1)
        dfs(x,y-1)

n,m = 4,5
graph=[]
for i in range(n):
    graph.apppend(list(map,input()))
result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) ==True: result+=1
print(result)        
