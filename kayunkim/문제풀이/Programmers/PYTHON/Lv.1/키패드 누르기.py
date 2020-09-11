def solution(numbers, hand):
    ans = ''
    cur = {'left':[3,0], 'right':[3,2]}
    keypad = [[3,1],[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
    for i in numbers:
        if i in [1,4,7]:
            ans+='L'
            cur['left'] = keypad[i]
        elif i in [3,6,9]:
            ans+='R'
            cur['right'] = keypad[i]
        else:
            useleft = abs(keypad[i][0]-cur['left'][0]) + abs(keypad[i][1]-cur['left'][1])
            useright = abs(keypad[i][0]-cur['right'][0]) + abs(keypad[i][1]-cur['right'][1])
            if useleft > useright:
                ans+='R'
                cur['right'] = keypad[i]
            elif useleft < useright:
                ans+='L'
                cur['left'] = keypad[i]
            else:
                ans+=hand[0].upper()
                cur[hand] = keypad[i]
    return ans