def ton(x):
    if x % 2 == 0: return x//2
    return x//2+1
def solution(n, a, b):
    answer = 1
    if a>b: a,b= b,a
    while True:
        if b % 2 == 0 and a + 1 == b: return answer
        a = ton(a)
        b = ton(b)
        answer += 1

