def solution(name):
    answer=0
    base=["A"]*len(name)
    idx=0
    while name !=base:
        right,left=1,1
        if name[idx]!='A':
            num =ord(name[idx]-ord['A'])
            if num>13:answer+=26-num
            else:answer+=num
            name[idx]='A'
        if name ==base:break
        for i in range(1,len(name)):
            if name[idx+i]=='A': right+=1
            else:break
            if name[idx-i]=='A': left+=1
            else:break
        if right>left:
            answer+=left
            idx-=left
        else:
            answer+=right
            idx+=right
    return answer
print(solution('JEROEN'))
            