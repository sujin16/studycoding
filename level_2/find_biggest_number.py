def arr_sum(i,j,size,arr):
    for j in range(j,j+size):
        if sum(arr[j][i:i+size]) !=size: return False
    return True
def solution(board):
    size = len(board[0]) if len(board)>=len(board[0]) else len(board)
    while True:
        if size ==0: return 0
        i,j =0,0
        while i+size-1<len(board[0]):
            while j+size-1<len(board):
                if arr_sum(i,j,size,board): return size*size
                j+=1
            i+=1;j=0
        size-=1
board=[[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]
print(solution(board))
