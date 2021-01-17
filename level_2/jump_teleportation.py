def solutiion(n):
    answer=0
    if not (n & (n - 1)):return 1
    while True:
        quo = n//2
        divison = n%2
        if divison !=0: answer+=1;n-=1
        n =quo
        if not (n & (n - 1)):answer+=1;break
    return answer


N=5000
print(solutiion(N))