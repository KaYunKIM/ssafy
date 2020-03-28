# 파일명 및 함수명을 변경하지 마시오.
# 추가 모듈이나 패키지를 import 할 수 없습니다.
def q6(number):
    """
  	아래에 코드를 작성하시오.
  	number는 양의 정수입니다.
  	number가 샌드위치 숫자를 포함하는 경우 True, 그렇지 않으면 False를 반환합니다. (Boolean)
  	"""

    ans = False
    number = str(number)
    if len(number)>=3:
        for i in range(1,len(number)-1):
            if number[i-1] == number[i+1]:
                ans = True
    return ans


# 실행 결과를 확인하기 위한 코드입니다. 수정하지 마시오.
if __name__ == '__main__':
    print(q6(8))
    print(q6(155))
    print(q6(1555))
    print(q6(2020))
    print(q6(414092133))