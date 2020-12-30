def  make_array(str):
    dat_array =[]
    array = list(str)
    print(array)
    for i,chr in enumerate(array):
        if i>1 and array[i-1] =='1' and array[i] =='0':
           del dat_array[-1]
           dat_array.append('10')
        else:
            dat_array.append(chr)
    return dat_array

def soultion(dartResult):
    answer =[]
    array =list(dartResult)
    dat_array =make_array(dartResult)
    print(dat_array)
    option =1
    for i, chr in enumerate(dat_array):
        if chr.isalpha():
            num = int(dat_array[i-1])
            if chr =='S': answer.append(pow(num,1))
            if chr =='D': answer.append(pow(num,2))
            if chr =='T': answer.append(pow(num,3))
        elif chr =='#':
            answer[-1]*=-1
        elif chr =='*':
            if len(answer) ==1 : answer[0]*=2
            else:
                answer[-1]*=2
                answer[-2]*=2
            
    return sum(answer)


    

dartResult = '10S'
print(soultion(dartResult))
