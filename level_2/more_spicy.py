import heapq
def solution(scoville,K):
    answer=0
    heapq.heapify(scoville)
    while True:
        if len(scoville) ==1 and scoville[0] <K: return -1
        if scoville[0] >= K :break
        num = heapq.heappop(scoville) +heapq.heappop(scoville)*2
        heapq.heappush(scoville, num)
        answer+=1
    return answer

scoville = [1,2,3,9,10,12]
K =7
print(solution(scoville,K))


