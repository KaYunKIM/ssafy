T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    pascal_1 = []
    for j in range(1, N + 1):
        pascal = [0] * j
        pascal_1.append(pascal)
    for x in range(len(pascal_1)):
        pascal_1[x][0] = 1
        pascal_1[x][-1] = 1
        if 3 <= len(pascal_1[x]):
            for y in range(len(pascal_1[x]) - 2):
                pascal_1[x][y + 1] = pascal_1[x - 1][y] + pascal_1[x - 1][y + 1]

print('#{}'.format(tc))
for p in pascal_1:
    print(' '.join(str(i) for i in p))