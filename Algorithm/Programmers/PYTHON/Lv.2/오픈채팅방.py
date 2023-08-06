def solution(record):
    ans = []
    renew = {}
    temp = []
    for i in record:
        i = i.split(' ')
        if i[0]=='Enter' or i[0]=='Change':
            renew[i[1]] = i[2]
    for j in record:
        j = j.split(' ')
        if j[0]=='Enter':
            ans.append(renew[j[1]]+'님이 들어왔습니다.')
        elif j[0]=='Leave':
            ans.append(renew[j[1]] + '님이 나갔습니다.')
    return ans