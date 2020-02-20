# 파일명 및 함수명을 변경하지 마시오.
# 추가 모듈이나 패키지를 import 할 수 없습니다.

def q5(number):

    num = str(number)
    first = num[:]

    if len(first) == 1 :
        return True
    
    for a in range(0, len(num)-1) :
        if abs(int(num[a]) - int(num[a+1])) != 1 :
            return False
    
    return True





# 실행 결과를 확인하기 위한 코드입니다. 수정하지 마시오.
if __name__ == '__main__':
    print(q5(8))
    print(q5(79))
    print(q5(5567))
    print(q5(4343456))
    print(q5(89098))