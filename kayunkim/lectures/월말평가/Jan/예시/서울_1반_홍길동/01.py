# 파일명 및 함수명을 변경하지 마시오.
# 추가 모듈이나 패키지를 import 할 수 없습니다.
def q1(number):
    """
    아래에 코드를 작성하시오.
    number는 0이 아닌 정수로 구성 되어있습니다.
    주어진 조건에 따라 Boolean 값인 True 혹은 False를 반환합니다.
    """
    if number > 0:
        return True
    if number <0:
        return False


# 실행 결과를 확인하기 위한 코드입니다. 수정하지 마시오.
if __name__ == '__main__':
    print(q1(3))
    print(q1(-8))

# 해설) 
# 1. python 01.py로 파이썬 파일을 실행하면 아래와 같은 출력값을 확인할 수 있습니다.
# 그리고, 이 내용은 문제 pdf 파일의 예시 입력 / 예시 출력과 동일합니다.
# True
# False

# 2. input 값이 0이 아닌 정수로 되어 있기 때문에, 0에 대한 예외 처리등은 진행할 필요가 없습니다.
