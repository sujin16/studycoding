from datetime import date,timedelta,datetime
def solution(lines):
    answer =0
    arr=[]
    for line in lines:
        date,clock_e,time =line.split(' ')
        clock_s = datetime.strptime(date+' '+clock_e, '%Y-%m-%d %H:%M:%S.%f')
        time =float(time[:-1])
        clock_s -=timedelta(milliseconds= time*1000 -1)
        clock_s = clock_s.strftime('%H:%M:%S.%f')[:-3]
        arr.append([clock_s,clock_e])
    arr.sort(key =lambda x : x[0])
    
    result=[] 
    print(arr)
    start =datetime.strptime(arr[0][0],'%H:%M:%S.%f')
    diff=1
    while True:
        result.append([0])
        cur =start
        for time in arr:
            s_time = datetime.strptime(time[0],'%H:%M:%S.%f')
            while True:
                if cur<=s_time<=cur+timedelta(seconds=diff):
                    result[diff-1][-1]+=1
                    break
                cur+=timedelta(seconds=diff)
                result[diff-1].append(0) 
                    
        
        if result[diff-1] ==[0]:break
        diff+=1
    return result
   
lines =	["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"]
print(solution(lines))