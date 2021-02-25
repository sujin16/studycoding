def solution(stones,k):
    answer=0
    minV,maxV = min(stones), max(stones)
    while True:
        mid = (minV+maxV)//2
        idx=0
        for stone in stones:
            if stone -mid<=0: idx+=1
            elif idx<k  and stone-mid>0: idx=0
            elif idx>k: break
        if idx ==k: return mid
        if idx<k: minV =mid+1
        if idx>k: maxV =mid-1



def solution2(stones,k):
    answer=0
    val = min(stones)
    while True:
        answer+=val
        
        for i in range(len(stones)):
            if stones[i] !=0: stones[i]-=val
        
        print(stones)
        idx =0
        val =1

        for i in range(len(stones)):
            if stones[i] ==0: idx+=1
            elif idx<k and stones[i]!=0:idx=0
            if idx ==k: return answer
            if stones[i] !=0 and val>stones[i]:val= stones[i]            

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))