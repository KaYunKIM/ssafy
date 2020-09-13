def solution(board, moves):
    ans = 0
    basket = []
    for i in moves:
        i-=1
        for line in board:
            if line[i]>0:
                if basket and basket[-1] == line[i]:
                    basket.pop()
                    ans+=2
                else:
                    basket.append(line[i])
                line[i] = 0
                break
    return ans