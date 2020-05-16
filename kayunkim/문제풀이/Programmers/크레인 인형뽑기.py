def solution(board, moves):
    answer = 0
    bin = []
    for j in moves:
        for i in range(len(board)):
            if board[i][j-1]!=0:
                if len(bin)==0 or bin[-1]!= board[i][j-1]:
                    bin.append(board[i][j-1])
                elif bin[-1]== board[i][j-1]:
                        bin.pop()
                        answer+=2
                board[i][j-1]=0
                break
    return answer