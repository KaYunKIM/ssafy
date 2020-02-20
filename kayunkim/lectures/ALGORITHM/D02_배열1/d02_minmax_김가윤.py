T = int(input())                 #Test case 개수 입력
for tc in range(1,T+1):          #Test case만큼 반복문 돌리기
    N = int(input())             #양수 개수 N 입력
    ai = list(map(int,input().split()))   #양수 ai 개수 입력 후 공백으로 나눠서 리스트로 만들기
    if len(ai) == N:             #만약 양수 ai의 개수가 N개라면.
        maximum = ai[0]          #최대값의 기준을 ai의 첫번 째 숫자로 둔다
        minimum = ai[0]          #최소값의 기준을 ai의 첫번 째 숫자로 둔다
        for x in range(1, N):    #첫번째 숫자인 기준점을 제외한 ai의 개수인 N만큼 반복한다
            if maximum < ai[x]:  #최대값의 기준점보다 현재 비교 값이 크다면,
                maximum = ai[x]  #최대값을 현재 값으로 변경한다
            if minimum > ai[x]:  #최소값의 기준점보다 현재 비교 값이 작다면,
                minimum = ai[x]  #최소값을 현재 값으로 변경한다
        D = maximum - minimum    #최대값과 최소값의 차이를 D라고 한다
        print('#{} {}'.format(tc,D))  #양식에 맞게 출력한다