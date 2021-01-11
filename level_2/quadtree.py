def solution(arr):
    cur_len =len(arr)
    sub_len = cur_len//2
    if cur_len ==2: 
        val =sum([sum(i) for i in arr]) 
        return [cur_len*cur_len-val,val]
    
    answer = [0]*2
    for i in range(0,cur_len,sub_len):
        for w in range(2):
            sub_arr =[]
            for j in range(sub_len):
                sub_arr.append(arr[j+sub_len*w][i:i+sub_len])
            val =sum([sum(i) for i in sub_arr]) 
            if val==0: answer[0]+=1 
            elif val== sub_len*sub_len: answer[1]+=1
            else: answer = [x+y for x,y in zip(answer,solution(sub_arr))]
    if answer[0] ==0: return [0,1]
    elif answer[1] ==0: return [1,0]
    return answer

arr =[
[1,1,1,1,1,1,1,1],
[0,1,1,1,1,1,1,1],
[0,0,0,0,1,1,1,1],
[0,1,0,0,1,1,1,1],
[0,0,0,0,0,0,1,1],
[0,0,0,0,0,0,0,1],
[0,0,0,0,1,0,0,1],
[0,0,0,0,1,1,1,1]]
print(solution(arr))
