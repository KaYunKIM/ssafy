# T = int(input())
# for tc in range(1,T+1):
#     org = input()
#     bin = [0]*len(org)
#     cnt = 0
#     # while bin != org:
#     for i in range(len(org)):
#         if int(org[i]) == 1:
#             bin[i:]=1
#         print(bin)
    #     elif org[i] == 0:
    #         bin[i:] =0
    #     print(bin)
    #     cnt += 1
    #     print(cnt)
    # print(cnt)

a= list(input().split())
bin = []
for i in a:
    if i=='I':
        bin.append([])
    elif i == 'D':

    elif i == 'A':
        print(i)



