import string 
def solution(name):
    answer=0
    cur = 0
    add =1
    for i in range(0,len(name),1):
        index = string.ascii_uppercase.index(name[i])
        print(index)
        if index ==0: continue
        else:
            if i -cur < cur+ len(name)- i: answer+=i -cur
            else: answer+= cur+ len(name)- i
        
            if index <=13: answer+=index
            elif index >13: answer+=26-index
            cur = i
    return answer
        


name ='CANAAAAANAN'
print(solution(name))