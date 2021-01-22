import re
dic={}
def split_str(file):
    num =''
    for i in range(len(file)):
        if len(num)>0 and file[i].isalpha():break
        if len(num) ==5:break 
        if file[i].isdigit():num+=file[i]
   
    head = file.split(num)[0]
    name = head+'_'+num+'_'
    if len(file.split(num)) ==2: name+=file.split(num)[1]
    key = head.lower()

    if key in dic.keys():
        arr= dic[key]
        for i in range(len(arr)):
            val =int(arr[i].split('_')[1])
            if int(num)<val:dic[key].insert(i,name);break
            if int(num)==val:dic[key].insert(i+1,name);break 
            if i ==len(arr)-1:dic[key].append(name)
    else: dic[key] =[name]
    
def solution(files):
    answer =[]
    for file in files: split_str(file)
        
    for key, value in sorted(dic.items()):
        for val in value:
            val =val.replace('_','')
            answer.append(val)
    return answer


files = ['img000012345', 'img1.png','img2','IMG02']
print(solution(files))