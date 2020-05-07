def babyjin(card,k):
    card.sort()
    if (8 in a and 9 in a and 0 in a) or (0 in a and 1 in a and 9 in a):
        return k

    for j in range(1,len(card)-1):
        if card[j-1]==card[j]==card[j+1] or (card[j-1]+1==card[j] and card[j]+1==card[j+1]):
            return k
        # print(b[j-1],b[j],a[j+1])

T = int(input())
for tc in range(1,T+1):
    num = list(map(int,input().split()))
    a = []
    b = []
    ans = 0
    for i in range(12):
        if i%2==0:
            a.append(num[i])
            if len(a)>= 3:
                if print(babyjin(a,1)) == 1:
                    ans = 1
                    break
        else:
            b.append(num[i])
            if len(b)>= 3:
                if print(babyjin(b, 2)) == 2:
                    ans = 2
                    break
    print('#{} {}'.format(tc,ans))

    # for i in range(12):
    #     if i%2==0:
    #         a.append(card[i])
    #         if len(a)>=3:
    #             for j in range(1,len(a)-1):
    #                 if abs(a[j-1]-a[j])+abs(a[j]-a[j+1])<=3 or a[j-1]==a[j]==a[j+1]:
    #                     ans=1
    #                     break
    #     else:
    #         b.append(card[i])
    #         if len(b) >= 3:
    #             for j in range(1,len(b)-1):
    #                 x = abs(b[j-1] - b[j])
    #                 y = abs(b[j] - b[j+1])
    #                 if abs(x-y)<=1:
    #                     ans=2
    #                     print(b[j-1],b[j],b[j+1])
    #                     break
    # print(ans)