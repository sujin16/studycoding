import json
def soultion(s):
    answer=[]
    s =s.replace('{','[')
    s =s.replace('}',']')
    s =json.loads(s)
    print(s)
    arr =sorted(s, key=len)
    for tu in arr:
        for i in range(len(tu)):
            if tu[i] not in answer :answer.append(tu[i])
    print(answer)
    return [int(i) for i in answer]
s = "{{1,2,3},{2,1},{1,2,4,3},{2}}"
print(soultion(s))