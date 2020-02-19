# 파일명 및 함수명을 변경하지 마시오.
# 추가 모듈이나 패키지를 import 할 수 없습니다.
def q3(number):
    """
    아래에 코드를 작성하시오.
    number는 세자리 양의 정수로만 구성 되어있습니다.
    number가 제시된 수학적 규칙에 해당하면 True, 그렇지 않으면 False를 반환합니다. (Boolean)
    """

    num = str(number)
    for i in range(1, len(num)+1):
        if int(num[-i:])%2==0:
            if int(num[-(i+1):])%3==0:
                if int(num[-(i+2):])%4==0:
                    return True
                else: 
                    return False
            else:
                return False       
        else:
            return False

# 실행 결과를 확인하기 위한 코드입니다. 수정하지 마시오.
if __name__ == '__main__':
    print(q3(512))
    print(q3(384))
    print(q3(321))