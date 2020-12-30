def distance(num, cur):
    dist =0
    arr =[ num//3,num%3]
    cur_arr =[cur[0],cur[1]]
    while arr!=cur_arr:
        for i in range(2):
            if arr[i]> cur_arr[i]:
                dist+=1
                cur_arr[i]+=1
            elif arr[i]<cur_arr[i]:
                dist+=1
                cur_arr[i]-=1
    return dist

def soultion(numbers,hand):
    answer=''
    left =[3,0]
    right = [3,2]
    for i in numbers:
        i-=1
        if i==-1 : i =10
        index = [i//3,i%3]
        
        print(index)
        if index[1] ==0:
            left = index
            answer+='L'
        elif index[1] ==2:
            right =index
            answer+='R'
        elif index[1] ==1:
            a = distance(i,left)
            b =distance(i,right)
            if a ==b:
                if hand =='left':
                    answer+='L'
                    left = index
                elif hand =='right':
                    answer+='R'
                    right = index
            elif a>b:
                answer+='R'
                right =index
            elif a<b:
                answer+='L'
                left= index
    return answer

numbers =[1,3,4,5,8,2,1,4,5,9,5]
hand='right'
print(soultion(numbers,hand))