import string 
dic ={ch:n+1 for n,ch in enumerate(string.ascii_uppercase)}

def make_arr(msg):
    arr =[]
    for i in range(0,len(msg)): arr.append(msg[0:len(msg)-i])
    return arr

def solution(msg):
    answer=[]
    msg_arr = make_arr(msg)
    while len(msg)>0:
        check =True
        i=0
        while check or i<len(msg):
            if msg_arr[i] in dic.keys():
                answer.append(dic[msg_arr[i]])
                check =False
                if i ==0: return answer
                dic[msg_arr[i-1]] =len(dic.keys())+1
                msg = msg[len(msg_arr[i]):]
                msg_arr =make_arr(msg)
                    
            i+=1

msg ='TOBEORNOTTOBEORTOBEORNOT'
print(solution(msg))