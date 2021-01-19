from datetime import datetime
import time
import operator

def make_melody(diff,string):
    arr=[]
    i =0
    while i<len(string):
        if i< len(string) -1 and string[i+1] =='#':arr.append(string[i:i+2]);i+=2
        else: arr.append(string[i]);i+=1
    
    melody =''
    for i in range(diff//len(arr)): melody+="".join(arr)
    melody+="".join(arr[:diff%len(arr)]) 
    return melody

def calc_time(s,e):
    fmt ='%H:%M'
    stime =datetime.strptime(s,fmt)
    etime =datetime.strptime(e,fmt)
    return int((etime-stime).seconds/60)

def solution(m,musicinfos):
    answer={}
    for music in musicinfos:
        stime,etime,title,info= music.split(',')
        diff = calc_time(stime,etime)
        melody =make_melody(diff,info)
        
        if m in melody:
            if m+'#' in melody: melody =melody.replace(m+'#','')
            idx =melody.find(m)
            if idx+len(m)<len(melody):
             if m[-1].isalpha() and  melody[idx+len(m)] =='#': continue 
            answer[title]=diff
        
    if len(answer.keys()) ==0: return '(None)'
    return max(answer.items(), key=operator.itemgetter(1))[0]


m='CDEFGAC'
musicinfos = ['12:00,12:06,HELLO,CDEFGA'] 
print(solution('ABC', ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))