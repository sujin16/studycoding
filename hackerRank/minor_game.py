from collections import defaultdict
def minion_game(string):
    #1.stuart #2.kevin
    stuartAarr,kevinArr=defaultdict(int),defaultdict(int)
    string = list(string)
    for i in range(len(string)):
        if string[i] in ('A', 'E', 'I', 'O', 'U'):
            for j in range(1,len(string)-i+1):
                key =''.join(string[i:i+j])
                kevinArr[key]+=1
        else:
            for j in range(1,len(string)-i+1):
                stuartAarr[''.join(string[i:i+j])]+=1
    print(stuartAarr)
    print(kevinArr)
    if sum(stuartAarr.values())>sum(kevinArr.values()):
        print('Stuart ',sum(stuartAarr.values()))
    else:
        print('Kevin ',sum(stuartAarr.values()))
        
    
string ='BANANA'
print(minion_game(string))