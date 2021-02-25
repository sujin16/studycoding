def make(a,b):
    if a*b==0:
        if a==0:a=b
        return [a,a*10,0]
    else:
        arr=[a+b,a*b,int(a/b),int(b/a),a-b,b-a]
        return list(set(arr))
def solution(N,number):
    if number ==N:return 1
    arr =make(N,N)
    arr.append(int(str(N)*(2)))
    arr_1=arr
    arr_2=[5]
    for i in range(2,9):
        if number in arr_1: return i
        else:
            new_arr=[int(str(N)*(i+1))]
            if (i+1)%2 ==0:
                for x in arr_2:
                    for y in arr_2:
                        new_arr+=make(x,y)
            else:
                 for x in arr_1:
                    for y in arr_2:
                        new_arr+=make(x,y)
            arr_2 =arr_1
            arr_1 =list(set(new_arr))
    return -1
print(solution(2,11))