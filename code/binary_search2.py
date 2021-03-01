from bisect import bisect_right,bisect_left
def soultion(arr,num):
    num =  bisect_right(arr,num) - bisect_left(arr,num)
    if num==0:return -1          
    return num
n=2
arr= [1,1,2,2,2,2,3]
print(soultion(arr,n))
