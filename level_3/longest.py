def solution(s):
    if len(s) ==1 or len(s) ==len(set(s)): return 1
    for i in range(len(s)-1):
        for j in range(i+1):
            origin = s[j:len(s)-i+j]
            if origin ==origin[::-1] :return len(s) -i
print(solution("abcde"))