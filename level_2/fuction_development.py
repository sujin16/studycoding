def solution(progress, speeds):
    answer=[]
    day=1
    idx =0 
    sub_idx =0
    while True:
        if sum(answer) ==len(progress):break    
        if idx ==len(progress): break
        if progress[idx] +speeds[idx]*day >=100:
            answer.append(1)
            idx +=1
            if idx ==len(progress): break
            sub_idx =idx
            while sub_idx !=len(progress):
                if progress[sub_idx]+speeds[sub_idx]*day >=100:
                    answer[-1]+=1
                    sub_idx+=1
                else:break
            idx =sub_idx
         
        day+=1

    return answer

progress =[95,90,99,99,80,99]
speeds=[1,1,1,1,1,1]
print(solution(progress,speeds))
