from itertools import permutations
def soultion(numbers,target):
    answer =0
    cur_list = [numbers[0],-numbers[0]]

    for i in range(1,len(numbers)):
        next = numbers[i]
        next_list =[]
        for num in cur_list:
            next_list.append(num+next)
            next_list.append(num-next)
        cur_list =next_list

    for num in cur_list:
        if num ==target: answer+=1
    
    return answer

n =[1,1,1,1,1]
target =5
print(soultion(n,target))