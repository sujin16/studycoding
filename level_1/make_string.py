s= "try  hello world"
index =0
answer =[]
for i,str in enumerate(s):
    if str.isalpha():
        if index%2 ==0: answer.append(str.upper())
        else: answer.append(str.lower())
        index+= 1
    else:
        index =0
        answer.append(" ")
print("".join(answer))
