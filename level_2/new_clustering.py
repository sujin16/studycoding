import math
def make_arr(str):
    str = str.lower()
    arr=[]
    for i in range(len(str)-1):
        string = str[i:i+2]
        if string.isalpha():arr.append(string)
    return arr

def make_dict(arr,dict):
    arr_dict = dict.copy()
    for i in range(len(arr)):
        for key in dict.keys():
            if key == arr[i]: arr_dict[key]+=1
    return arr_dict

def soultion(str1,str2):
    answer=1
    arr1,arr2 =make_arr(str1),make_arr(str2)
    if len(arr1) ==0 and len(arr2) ==0: return 65536
    elif len(arr1)*len(arr2)==0: answer =0

    arr =arr1+arr2
    dictOfWords = { arr[i] : 0 for i in range(len(arr1+arr2) ) }
    dictOfArr1 =make_dict(arr1,dictOfWords)
    dictOfArr2 =make_dict(arr2,dictOfWords)
    
    print(dictOfWords)
    print(dictOfArr1)
    print(dictOfArr2)
    
    a,b =0,0
    
    for key in dictOfWords.keys():
        value_1,value_2 =dictOfArr1[key],dictOfArr2[key] 
        print(value_1)
        if value_1 ==value_2 :a+=value_1;b+=value_1
        elif value_1>value_2: a+=value_2;b+=value_1
        elif value_1<value_2: a+=value_1;b+=value_2
    
    return math.trunc((a/b)*65536)

str1 ="E=M*C^2"
str2 ='e=m*c^2'
print(soultion(str1,str2))
