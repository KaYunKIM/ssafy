def solution(array, commands):
    ans = []
    for i in commands:
        ans.append(sorted(array[i[0]-1:i[1]])[i[2]-1])
    return ans