def solution(n,words):
    answer=[0,0]
    dict_arr =[]
    for i in range(0,len(words),n):
        if i+n >=len(words): arr =words[i:]
        else: arr =words[i:i+n]
        for j in range(n):
            word =words[i+j]
            if i+j >0 and words[i+j-1][-1] !=word[0]:
                return [j+1,i//n+1]

            if word in dict_arr:
                return [j+1,i//n+1]
            dict_arr.append(words[i+j])

n =2
words =['hello', 'one', 'even', 'never', 'now', 'world', 'draw']
print(solution(n,words))