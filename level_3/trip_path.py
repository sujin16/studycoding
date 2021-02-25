def make(a,b,graph):
    if a in graph.keys(): graph[a].append(b)
    else: graph[a] =[b]

def solution(tickets):
    graph={}
    for city in tickets:
        make(city[0],city[1],graph)
    for key,val in graph.items():
        graph[key].sort()
   

    path =['ICN']
    cur ='ICN'
    while len(tickets)>0:
        if len(graph[cur])>0:
            next = graph[cur].pop(0)
            path.append(next)
            tickets.remove([cur,next])
            cur =next

    return path
    
tickets =	[['ICN', 'A'], ['ICN', 'A'], ['A', 'ICN'], ['A' , 'C'] ]
print(solution(tickets))