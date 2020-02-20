def promissing():       #체스말을 놓을 수 있는지 없는지 판단하는 함수
    #같은 열, 같은 대각선 여부 판단: True False 리턴
    pass
def queen(level):
    if promissing() == False:
        return
    pass
    #재귀호출로 각 행에 체스를 놓기

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    matrix = [0]*(N+1)      #1~N행 : 몇번 째 열에 체스가 놓여있는지 ex) matrix[1] = 2
    queen()