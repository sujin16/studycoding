from math import gcd

def soultion(w,h):
    num = gcd(w,h)
    a = w//num
    b = h//num
    ratio =b/a
    answer=0
    
    for i in range(1,a):
        for j in range(b):
            if j>i*ratio:
                answer+= b-j
                break

    answer*=2
    print(answer)
    answer= a*b -answer
    return w*h - answer*num


print(soultion(1,8))

