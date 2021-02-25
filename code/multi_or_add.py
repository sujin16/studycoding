def solution(s):
    result=0
    s = list(map(int, [c for c in s]))
    while s:
        if s[0]*s[1] ==0:result=s[0]+s[1]
        else: result =s[0]*s[1]
        del s[0];del s[0]
        if len(s) ==0: break 
        else: s.insert(0,result)
        
    return result
def answer(s):
    s = list(map(int, [c for c in s]))
    result =s[0]
    for i in range(1,len(s)):
        if s[i]*result==0:result+=s[i]+result
        else: result*=s[i]
    return result
s='02984'
print(answer(s))
