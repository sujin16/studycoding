def soultion1(a,m):
    minV = max(a)+1
    val =0
    while val<m:
        val=0
        minV-=1
        for num in a:
            val+= num-minV if num>minV else 0
                
    return minV

##이진탐색
def soultion(a,m):
    result=0
    start,end= 0,max(a)
    while(start<=end):
        mid = (start+end)//2
        sumV=0
        for num in arr:
            sumV+=num-mid if num>mid else 0
        
        if sumV<m:end =mid-1
        else:
            result=mid
            start=mid+1

    return result

n,m = 4,6
arr= [19,15,10,17]
print(soultion(arr,m))
