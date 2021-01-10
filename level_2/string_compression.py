def compression(size,string):
    s =string
    answer = list([s[i:i+size] for i in range(0, len(s), size)])
    arr =[1]*len(answer)
    i=0
    while i<len(answer)-1:
        if answer[i] ==answer[i+1]: del answer[i];del arr[i+1];arr[i]+=1
        else: i+=1 
    result =''
    for i in range(len(arr)):
        if arr[i] != 1 :result+=str(arr[i])+answer[i]
        else: result+=answer[i]
    print(result)
    return len(result)
    
def solution(s):
    size = int(len(s)/2)
    if len(s) ==1: size =1
    min= compression(size,s)
    size-=1 
    while size>0:
        num = compression(size,s)
        if min> num : min = num 
        size-=1
    return min
s ='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxz'
print(solution(s))