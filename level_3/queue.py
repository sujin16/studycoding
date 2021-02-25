import heapq
def soultion(operations):
    heap =[]
    for oper in operations:
        a,b =oper.split(' ')
        if a =='I':heapq.heappush(heap,int(b))
        else: 
            if len(heap) ==0:continue
            if oper =='D -1': heapq.heappop(heap)
            if oper =='D 1':del heap[-1]

    if len(heap) ==0:return [0,0]
    return [heap[-1],heap[0]]
operations =	["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
print(soultion(operations))