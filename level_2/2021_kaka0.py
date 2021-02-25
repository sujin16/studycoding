from itertools import combinations
def solution(infos,query):
    answer =[0]*len(query)

    for i, condi in enumerate(query):
        condi = condi.replace(' and ',' ')
        condi =condi.split(' ')
        num=0
        for info in infos:
            info =info.split(' ')
            check=False
            for j in range(5):
                if j ==4 and (condi[j]=='-' or int(info[j])>=int(condi[j])): check=True
                if condi[j]!='-' and condi[j] !=info[j]:break

            if check:num+=1
        answer[i]=num
    return answer

info=["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150", "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"]
query=["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200", "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]
print(solution(info,query))

'''
from itertools import combinations
a="java backend junior pizza 150"
a =a.split(' ')
print(a)
score =a[-1]
a= a[:-1]
for i in range(1,4):
    combi = list(combinations(a,i))
    print(combi)
'''