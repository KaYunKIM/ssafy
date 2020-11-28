def solution(name):
    answer = -1
    cur = ord('A')
    if 'A' in name:
        answer+=min(ord(name[0])-65, 90-ord(name[0])+1)
        answer+=1
        for i in range(len(name)-1,0,-1):
            if name[i] != 'A':
                answer+=min(ord(name[i])-65, 90-ord(name[i])+1)
                # print(ord(name[i])-65, 90-ord(name[i])+1,answer)
                answer+=1
    else:
        for i in range(len(name)):
            answer+=min(ord(name[i])-65, 90-ord(name[i])+1)
            # print(ord(name[i])-65, 90-ord(name[i])+1,answer)
            answer+=1
    return answer