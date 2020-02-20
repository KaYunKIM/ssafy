# T = int(input())
#
# for tc in range(1,T+1):
#     str1 = input()
#     str2 = input()
#
#     bin = {}
#     for i in range(len(str1)):
#         cnt = 0
#         for j in range(len(str2)):
#             if str1[i] in str2[j]:
#                 cnt+=1
#                 bin[str1[i]] = cnt
#     max = 0
#     for i in bin:
#         if max < bin[i]:
#             max = bin[i]
#
#     print('#{} {}'.format(tc,max))


def maxV(str1, str2):

    bin = {}
    for i in range(len(str1)):
        cnt = 0
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                cnt+=1
                bin[str1[i]] = cnt

    max1 = 0
    for i in bin:
        if max1 < bin[i]:
            max1 = bin[i]

    return max1

T = int(input())
for tc in range(1,T+1):
    str1 = input()
    str2 = input()

    print('#{} {}'.format(tc, maxV(str1,str2)))