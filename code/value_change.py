def solution(a,b):
    a.sort()
    b.sort(reverse=True)
    i=0
    while i<k :
        if a[i] <b[i]:
            a[i],b[i]= b[i],a[i]
            i+=1
    return sum(a)

n,k = 5,3
a=[1,2,5,4,3]
b=[5,5,6,6,5]
print(solution(a,b))
