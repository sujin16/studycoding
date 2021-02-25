def solution(arr):
    arr.sort()
    result,count =0,0
    for i in arr:
        count+=1
        if count>=i: 
            result+=1
            count=0
    return result
arr = [2,3,1,2,2]
print(solution(arr))
