# 파일명 및 함수명을 변경하지 마시오.
# 추가 모듈이나 패키지를 import 할 수 없습니다.
def q5(number):
    """
  	아래에 코드를 작성하시오.
  	number는 양의 정수입니다.
  	number가 계단식 숫자일 경우 True, 그렇지 않으면 False를 반환합니다. (Boolean)
  	"""

    ans = True
    number = str(number)
    if len(number) == 2:
        if abs(int(number[0]) - int(number[1])) != 1:
            ans = False

    elif len(number) >2:
        for i in range(1,len(number)-1):
            if abs(int(number[i])-int(number[i-1])) != 1 or abs(int(number[i])-int(number[i+1])) != 1:
                ans = False
    return ans


# 실행 결과를 확인하기 위한 코드입니다. 수정하지 마시오.
if __name__ == '__main__':
    print(q5(8))
    print(q5(79))
    print(q5(5567))
    print(q5(4343456))
    print(q5(89098))