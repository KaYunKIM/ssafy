def solution(transaciton, data):
    answer = []
    V = []
    for i in transaction:
        account = int(i[1])
        ans = i[0]
        visited = []
        for j in data:
            if j[0] not in visited:
                visited.append(j[0])
                if j[2] == ans:
                    if j[1] == "SAVE":
                        account+=int(j[3])
                    else:
                        account-=int(j[3])
                    V.append(j[0])
        answer.append([ans,str(account)])
    if j[0] not in V and j[0]!= ans:
        answer.append([j[2],j[3]])
    return answer

transaction = [
    ["ACCOUNT1", 100],
    ["ACCOUNT2", 150]
    ]
data = [
    ["1","SAVE","ACCOUNT2", "100" ],
    ["2","WITHDRAW","ACCOUNT1","50"],
    ["1","SAVE","ACCOUNT2", "100" ],
    ["3","WITHDRAW","ACCOUNT2", "30" ],
    ["4","SAVE","ACCOUNT3", "150" ]
]
print(solution(transaction,data))