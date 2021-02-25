def solution(a,b):
    count=0
    if a+2<9 and b+1<9:count+=1
    if a+2<9 and b-1>0:count+=1
    if a-2>0 and b+1<9:count+=1
    if a-2>0 and b-1>0:count+=1
    return count
    
a = ord('a')-96
b =1
count=solution(a,b)+solution(b,a)
print(count)

# answer
cur = input()
row,col =int(cur[0]),ord(cur[1])-96
steps=[(-2,-1),(-2,1),(2,-1),(2,1),(1,2),(1,-2),(-1,-2),(-1,2)]
result=0
for step in steps:
    nextr,nextc = row+step[0],row+step[1]
    if 1<=rextr<=8 and 1<=nextc<=8: result+=1
print(result)
