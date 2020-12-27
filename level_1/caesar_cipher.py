def solution(s,n):
    s = list(s)

    for i in range(len(s)):
        n = n%26
        if s[i].isupper():
           s[i]= chr(ord('A')+ ord(s[i])+n - ord('A'))
        elif s[i].islower():
            num = (ord(s[i])- ord('a')+n)%26 +ord('a')
            s[i] = chr(num)
    
    return "".join(s)

s ="A B"
print(solution(s,1))