def solution(arrangement):
    ans = 0  ##조각개수
    temp = 1   #막대기 개수
    for a in range(1,len(arrangement)):
        if arrangement[a] == '(':
            temp+=1
        else:
            if arrangement[a-1]=='(':
                temp-=1
                ans+=temp
            else:    #'))'
                temp-=1
                ans+=1
    return ans


def solution(arrangement):
    ans = 0
    temp = 0
    transform = arrangement.replace('()','0')
    for t in transform:
        if t=='(':
            temp+=1
        elif t==')':
            ans+=1
            temp-=1
        else:
            ans+=temp
    return ans



def solution(arrangement):
    ans = 0
    temp = []
    cnt = [0]*len(arrangement)
    cur = 0
    end = 0
    state = 'open'
    add = []
    for i in range(len(arrangement)):
        if arrangement[i] == '(':
            if state== 'open':
                open = i-1
            state = 'open'
            temp.append(arrangement[i])
            add.append(i)
            cnt[i]=1
            print('1',cnt)
        else:
            temp.pop()
            if state == 'close':
                end = i+1
                print('3',cnt)
                print(i,k,close,open,add,end)
                ans+=cnt[add[-1]]
                cnt[add[-1]]=0
                print(ans)
            if temp:
                close = i
                for k in range(end,i):
                    if cnt[k]:
                        cnt[k]+=1
                print('2',cnt)
            else:
                end = i+1
            cnt[i-1]=0
            cur = i+1
            state = 'close'
            add.pop()
    return ans