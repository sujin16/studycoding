from itertools import permutations
from copy import copy
import re
operaters =[list(t) for t in permutations(['*','+','-'])]

def calc(string,arr):
    for oper in arr:
        idx=0
        while idx<len(string):
            if string[idx] ==oper:
                num = "".join(string[idx-1:idx+2])
                string[idx-1] =str(eval(num))
                del string[idx:idx+2]
            else: idx+=1
    return int(string[0])

def soultion(expression):
    expression= re.findall('\d+|\D+', expression)
    arr=[]
    for oper in operaters:
        arr.append(abs(calc(copy(expression),oper)))

    return max(arr)
               


        
expression= "100-200*300-500+20"
print(soultion(expression))