def solution():
    n = int(input())
    for i in range(n):
        networks=set()
        m =int(input())
        for j in range(m):
            a,b =map(str,input().split())
            networks.add(a)
            networks.add(b)
            print(len(networks))

solution()