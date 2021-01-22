class G:
    pending = set()
    bombed = 0
    board = []
def bomb():
    for i, j in reversed(sorted(G.pending)):
        G.board[i].pop(j)
        G.bombed += 1
    G.pending = set()

def traverse(i, j):
    print(G.board[i+1])
    if j >= len(G.board[i+1]) - 1:
        return

    if G.board[i][j] == G.board[i][j+1] == G.board[i+1][j] == G.board[i+1][j+1]:
        for x, y in [(i + 1, j + 1), (i + 1, j), (i, j + 1), (i, j)]:
            G.pending.add((x, y))


def solution(m, n, board):
    G.board = [[board[i][j] for i in reversed(range(m))] for j in range(n)]
    
    while True:
        for i in range(len(G.board) - 1):
            for j in range(len(G.board[i]) - 1):
                traverse(i, j)
        if not G.pending:
            break
        bomb()

    return G.bombed

m,n =4,5
board=["CCBDE", "AAADE", "AAABF", "CCBBF"]
print(solution(m,n,board))