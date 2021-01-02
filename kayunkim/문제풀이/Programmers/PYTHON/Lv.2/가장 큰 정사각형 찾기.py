import itertools

def solution(board):
    M, N = len(board), len(board[0])
    for i in range(1, M):
        for j in range(1, N):
            if board[i][j] == 1:
                board[i][j] = min(board[i-1][j-1], board[i-1][j], board[i][j-1]) + 1
                print(board)

    return max(itertools.chain(*board))**2