## 75
def solution(tickets):
    answer = []
    airport = {}
    for ticket in tickets:
        if ticket[0] not in airport:
            airport[ticket[0]] = [ticket[1]]
        else:
            airport[ticket[0]].append(ticket[1])

    stack = ["ICN"]
    while stack:
        dpt = stack.pop()
        answer.append(dpt)

        if dpt in airport:
            if len(airport[dpt]) == 1:
                stack.append(airport[dpt][0])
                del airport[dpt]

            else:
                airport[dpt].sort()
                for i in airport[dpt]:
                    if i in airport:
                        stack.append(i)
                        airport[dpt].remove(i)

    return answer점


## 정답
def solution(tickets):
    answer = []
    tickets.sort()

    airport = {}
    for dpt, arv in tickets:
        if dpt not in airport:
            airport[dpt] = [arv]
        else:
            airport[dpt].append(arv)

    stack = ["ICN"]
    while stack:
        dpt = stack[-1]
        if dpt not in airport or not airport[dpt]:
            answer.append(stack.pop())
        else:
            stack.append(airport[dpt].pop(0))

    return answer[::-1]