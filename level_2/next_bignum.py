def solution(n):
    num =list(bin(n)).count('1')
    i =1
    while True:
        n+=1
        if list(bin(n)).count('1') ==num:return n
n=15
print(solution(n))