from itertools import chain
def soultion(n):
    maps = [[0 for _ in range(n)] for _ in range(n)]
    y,x =-1,0
    value =1
    for i in range(n):
        for j in range(i,n):
            if i%3 ==0: y+=1
            if i%3 ==1: x+=1
            if i%3 ==2: y-=1;x-=1
            
            maps[y][x] =value
            value+=1
        
    return [i for i in chain(*maps) if i !=0]
n=5
print(soultion(n))