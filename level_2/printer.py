def solution(priorites, locatoin):
    answer=0
    arr={}
    for i in priorites : arr[i] =[]
    for i, pri in enumerate(priorites): arr[pri].append(i)
        
    arr =  dict(sorted(arr.items(), reverse =True))
    print(arr)
    
    cur =-1
    for key,value in arr.items():
        if cur == -1:
            for i, var in enumerate(value):
                if i+1 ==len(value): cur = var
        else:
            a =[]
            b=[]
            for i,var in enumerate(value):
                if cur >var: a.append(var)
                else: b.append(var)
            arr[key] =b+a
            cur =arr[key][-1]
        
        print(cur)
    
    idx= 0
   
    for key, value in arr.items():
        for var in value:
            idx+=1
            if var ==location: 
                answer=idx
    
    return answer

priorites = [2,1,3,2]
location = 0
print(solution(priorites,location))