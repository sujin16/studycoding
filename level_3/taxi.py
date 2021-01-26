def floyd_warshall(n, edges):
    adj = [[float('inf')] * (n+1) for _ in range(n+1)] 
    
    for u, v, w in edges:
        adj[u][v] = w
        adj[v][u] = w
        
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
            	adj[i][j] = min(adj[i][j], adj[i][k] + adj[k][j])
    
    return adj

def solution(n,s,a,b,fares):
    answer = float('inf')
    dist = floyd_warshall(n,fares)
    for i in range(1,n+1):
        cost = dist[s][i] +dist[i][a] +dist[i][b]
        if answer>cost: answer =cost

    return answer
fares= [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
print(solution(6, 4, 6, 2, fares))