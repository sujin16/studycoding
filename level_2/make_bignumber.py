def solution(number,K):
    arr = list(number)
    max_arr= sorted(arr,reverse=True)
    answer=''
    length = len(number)-K

    while True:
        for j in range(len(max_arr)):
            if arr[0] >max_arr[j]:
                answer+=str(arr[0])
                arr= arr[1:]
                break
            
            elif max_arr[j] in arr:
                index =arr.index(max_arr[j]) 
                if length -len(answer) <= len(arr)-index: 
                    answer+=str(arr[index])
                    arr= arr[index+1:]
                    break    
            
        if len(answer) ==length: break
    return answer

number='1231234'
K=3
print(solution(number,K))



