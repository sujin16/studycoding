def solution(board):
    arr=[0]*len(board[0])
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] ==1: arr[j]+=1

    max_size =max(arr)
    if max_size ==0: return 0
    
    while max_size>0:
        index =[]
        print(max_size)
        for i in range(len(arr)):
            if max_size >=arr[i]:
                if len(index) ==0: index.append(i)
                elif index[-1] ==i+1: index.append(i)
        if len(index) ==max_size: return max_size*max_size
        max_size-=1
        



board=[[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]
print(solution(board))
