# def fix():
#     if N == 1:
#         return
#     else:
#         return


T = 10
for tc in range(1,T+1):
    N = int(input())
    pwd = list(map(int,input().split()))
    odn = int(input())
    order = list(input().split())
    bin = []
    for i in range(odn):
        if order[i] == 'I':
            bin.append(order[i:i+int(order[i+2])+3])
        elif order[i] == 'D':
            bin.append(order[i:i+3])
        elif order[i] == 'A':
            bin.append(order[i:i+int(order[i+1])+2])
    # for i in bin:
    #     if i[0] == 'I':
    pwd.insert(1,bin[0][3:])
        # elif i[0] == 'D':
        #
        # else:
    print(''.join(map(int(pwd))))