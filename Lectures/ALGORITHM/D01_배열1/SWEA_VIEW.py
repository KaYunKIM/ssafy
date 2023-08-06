# 기준 빌딩 주변의 빌딩 중 가장 높은 빌딩 찾기
# 기준 빌딩이 주변빌딩 최고층 빌딩 보다 높아면 둘의 차이를 구한다
import sys
sys.stdin = open('input.txt', 'r')   #표준입력 파일로 변경/ #디버깅용으로만 사용. 시험제출시 빼면 됨

#풀이
T =  10
for tc in range(1, T+1):
    N = int(input())          #빌딩 수
    H = list(map(int, input().split()))     #빌딩 높이 입력받아서 'H'배열에 저정하기
    view = 0    # 조망권 수
    for i in range(2, N-2):    #앞 뒤로 2칸은 빌딩이 없으므로
        # left = H[i-2] if (H[i-2]> H[i-1]) else H[i-1]
        # right= H[i+2] if (H[i+2]> H[i+1]) else H[i+1]
        # round_max = left if (left > right) else right
        round-max = max(h[i-2], h[i-1], h[i+1], h[i+2])   # 파이썬 max함수 써서 최대값 찾기
        if(H[i]> round_max):              # 주변 빌딩 최고층이 기준빌딩보다 낮으면
            view += (H[i] - round_max)    # 조망권 세대 수 누적 합
    print('#{} {}'.format(tc, view))

#연습
# for tc in range(1 + 11):
#     N = int(input())
#     H = list(map(int, input().split()))
#     sum = 0
#     for i in range(2, N-2):
#         left = H[i-1] if (H[1-1] > H[i-2]) else H[i-2]
#         right = H[i-1] if (H[1-1] > H[i-2]) else H[i-2]
#         round_max = left if left > right else right
#         round_max1 = max(H[i-1], H[i-2], H[i+1], H[i+2])
#         if H[i] > round_max:
#             sum += (H[i] -round_max1)
#     print('#{} {}'.format(tc, sum))