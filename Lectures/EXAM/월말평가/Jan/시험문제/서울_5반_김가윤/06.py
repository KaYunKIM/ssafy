# 파일명 및 함수명을 변경하지 마시오.
# 추가 모듈이나 패키지를 import 할 수 없습니다.
def q6(number):

    
    num = str(number)
    if 3> len(num):
        return False
    elif len(num)== 3:
        if int(num[0]) == int(num[2]):
            return True
        else:
            return False
    else:
        for i in range(1, len(num)):
            if int(num[i-1]) == int(num[i+1]):
                return True
            else:
                for j in range(1,i):
                    if int(num[(i-1+j)]) == int(num[(i+1+j)]):
                        return True
                    else:
                        return False


# 실행 결과를 확인하기 위한 코드입니다. 수정하지 마시오.
if __name__ == '__main__':
    print(q6(8))
    print(q6(155))
    print(q6(1555))
    print(q6(2020))
    print(q6(414092133))