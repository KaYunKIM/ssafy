#부분집합의 합이 10인 부분집합의 갯수 구하기
#완전탐색

def f(i,N,K):       #i번째 원소를 포함하는 경우/ 포함하지 않은 경우 -> 재귀호출
    global bit
    global cnt
    if i == N:      #base case : bit의 모든 칸이 결정됨
        s = 0
        for j in range(N):
            if bit[j] == 1:     #j번째 원소가 선택됨
                s+= j+1         #선택된 원소의 누적합
        if s == K:              #누적합 s가 K(10)과 같다면
            cnt+=1
        return
    else:
        bit[i] = 1  #i번째 원소 선택
        f(i+1,N,K)
        bit[i] = 0  #i번째 원소 선택 안함
        f(i+1,N,K)
N = 10      #원소수
K = 10      #부분집합의 합
bit = [0]*N     #원소의 포함여부 저장
cnt = 0         #조건을 만족하는 부분집합의 갯수

f(0,N,K)        #부분집합을 구하고 -> 총합이 10인 부분집합 갯수 세기
print(cnt)