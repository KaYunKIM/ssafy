#분할정복
#큰 문제를 해결할 수 있는 작은 문제로 분할하여 정복해 나가는 기법
#카드가 한장될 때까지 나눔
    #find() : 각 토너먼트에서 이긴 카드에 대해서 승부하기
    #카드가 한장될 때까지 나눔 -> 재귀호출

def find(l,r):   #ㅣ: 왼쪽, r: 오른쪽 => 카드리스트 범위
    if l ==r:    #카드가 한장일 때
        return l
    else:        #그렇지 않으면
        result1 = find(l,(l+r)//2)      #카드를 반으로 나눠 재귀 호출
        result2 = find((l+r)//2+1,r)
        if card[result1] == card[result2]:      #카드가 서로 같으면
            return result1
        else:                                   #같지 않으면
            #가위바위보 승부
            #가위:1, 바위:2, 보:3
            if card[result1] == 1 and card[result2]==2:
                return result2
            if card[result1] == 1 and card[result2]==3:
                return result1
            if card[result1] == 2 and card[result2]==1:
                return result1
            if card[result1] == 2 and card[result2]==3:
                return result2
            if card[result1] == 3 and card[result2]==1:
                return result2
            if card[result1] == 3 and card[result2]==2:
                return result1

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    card = [0] + list(map(int,input().split()))
    print('#{} {}'.format(tc,find(1,N)))
