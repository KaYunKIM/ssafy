T = int(input())                    #Test case 숫자 입력

for tc in range(1, T+1):            #Test case 개수만큼 반복하기
    N = int(input())                #카드 장수 N 입력
    V = list(map(int, input()))     #N개의 숫자 ai 입력
    cnt = [0]*10                    #카드의 개수를 누적해서 입력할 길이 (0~9)10의 빈 리스트 만들기
    max = 0                         #enumerate함수에서 이용할 x에 해당하는 max 변수 0으로 초기화
    id = 0                          #enumerate함수에서 이용할 y에 해당하는 id 변수 0으로 초기화

    for i in V:                     #N개의 숫자가 들어있는 리스트에 해당하는 i만큼 반복하기
        cnt[i] += 1                 #i 숫자를 만날 때 빈 리스트의 i자리수에 +1해주기

    for x,y in enumerate(cnt):      #빈 리스트를 enumerate함수를 사용해 반복하기
        if id <= y:                 #초기 값과 비교해 y의 값이 크다면,
            id = y                  #id값을 해당 y로 바꿔주기 => id의 최대값 반영
            max = x                 #최대값 id의 짝에 맞는 카드 숫자를 가져오기

    print('#{} {} {}'.format(tc, max, id))  #양식에 맞게 출력하기