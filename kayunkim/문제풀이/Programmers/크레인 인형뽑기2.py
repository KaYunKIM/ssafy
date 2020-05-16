def select(j,pan,bin):
    cnt = 0
    if len(bin)==0:
        for i in range(len(pan)):
            if pan[i][j]!=0:
                bin.append(pan[i][j])
                break
    else:
        for i in range(len(pan)):
            if bin[-1] == pan[i][j]:
                bin.pop()
                cnt+=2
            elif pan[i][j]!=0:
                bin.append(pan[i][j])
    return cnt

def solution(board, moves):
    ans=0
    bin = []
    for col in moves:
        ans+=select(col-1,board, bin,)
    return ans

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
print(solution(board,moves))