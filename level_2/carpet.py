from math import sqrt
def solution(brown, yellow):
    sum =brown+yellow
    height =3
    width =0
    while True:
        if sum%height ==0:
            width = sum//height 
            if yellow ==(height-2)*(width -2): return [width,height]
        height+=1
brown= 24
yellow =24
print(solution(brown,yellow))
