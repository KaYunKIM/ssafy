# 파일명 및 함수명을 변경하지 마시오.
# 추가 모듈이나 패키지를 import 할 수 없습니다.
def q1(number):
    """
    아래에 코드를 작성하시오.
    number는 양의 정수로 구성 되어있습니다.
    주어진 순서도의 조건에 따라 Boolean 값인 True 혹은 False를 반환합니다.
    """

    if number % 2 == 0 :
        return True
    return False



# 실행 결과를 확인하기 위한 코드입니다. 수정하지 마시오.
if __name__ == '__main__':
    print(q1(3))
    print(q1(8))