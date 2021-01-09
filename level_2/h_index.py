def solution(citation):
    citation.sort(reverse =True)
    answer=0
    for i,num in enumerate(citation):
        if answer>=num and answer==i : break
        answer+=1 
    return answer


citation = [3,0,6,1,5]
print(solution(citation)) 