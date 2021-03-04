import heapq
n,m,city =3,2,1
INF = float('inf')
distance = [INF]*(n+1)
graph=[[],[(2,4),(3,2)],[],[]]

def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start] =0
    while q:
        dist,now = heapq.heappop(q)
        if distance[now] <dist:continue
        for v,cost in graph[now]:
            cost+=dist
            if distance[v]>cost:
                distance[v] =cost
                heapq.heappush(q,(cost,v))

dijkstra(city)
a,b=0,0
#동시에 보내니까 최대 b 
for i in range(1,n+1):
    if i!=city and distance[i]!=INF:
        a+=1
        b = max(b,distance[i])
print(a,b)
    
             
