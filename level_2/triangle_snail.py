def soultion(n):
    answer =[0]*sum([ i for i in range(1,n+1)])
    count =1
    index =0
    value =1
    num2=0
    while n>0:
        if count%3 ==1:
            for i in range(0,n):
                index+=i+num2
                answer[index]= value
                value+=1
                
        if count%3 ==2:
            for i in range(0,n):
                index+=1
                answer[index] =value
                value+=1
                
        if count %3 ==0:
            for i in range(0,n):
                index-= count+n-num2//2 -i -1
                answer[index] =value
                value+=1
            num2+=2

        count+=1
        n-=1
    return answer

n =7
print(soultion(n))