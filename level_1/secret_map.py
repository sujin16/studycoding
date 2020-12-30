def make(arr,n):
    while len(arr) != n:
        arr.insert(0,'0')

def solution(n,arr1,arr2):
    answer=[]
    arr1= [bin(i)[2:] for i in arr1]
    arr2 =[bin(i)[2:] for i in arr2]
    for i in range(n):
        str=''
        str_1 = list(arr1[i])
        make(str_1,n)
        str_2 =list(arr2[i])
        make(str_2,n)
        print(str_1)
        print(str_2)
        for j in range(n):
            if str_1[j] =='1' or str_2[j] == '1': str+='#'
            elif str_1[j] =='0' and str_2[j] =='0': str+=' '
        answer.append("".join(str))
    return answer
    


arr1 =[9,20,28,18,11]
arr2 =[30,1,21,17,28]
n =5
print(solution(n,arr1,arr2))