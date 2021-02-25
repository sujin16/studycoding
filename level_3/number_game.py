import heapq
def solution(A,B):
    answer=0
    A.sort()
    heapq.heapify(B)
   
    for i in range(len(A)):
        if len(B)==0:break
        num = heapq.heappop(B)
        if A[i] ==num: continue
        if A[i]<num:
            answer+=1
        if A[i]>num:
            if A[i]>B[-1]: return answer
            while B:
                num = heapq.heappop(B)
                if A[i]==num:break
                if A[i]<num:answer+=1;break
    return answer

print(solution(	[2, 2, 2, 2], [1, 1, 1, 1]))