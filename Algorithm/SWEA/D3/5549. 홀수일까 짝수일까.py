T = int(input())
for tc in range(1,T+1):
    num = int(input())
    if num%2==0:
        print('#{} Even'.format(tc))
    else:
        print('#{} Odd'.format(tc))