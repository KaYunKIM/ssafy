# 파일명 및 함수명을 변경하지 마시오.
# 추가 모듈이나 패키지를 import 할 수 없습니다.
def q6(number):

    a= str(number)

    if len(a) <= 2 :
        return False

    for i in range(0,len(a)-2) :
        if int(a[i]) == int(a[i+2]) :
            return True

    return False 


  	





# 실행 결과를 확인하기 위한 코드입니다. 수정하지 마시오.
if __name__ == '__main__':
    print(q6(8))
    print(q6(155))
    print(q6(1555))
    print(q6(2020))
    print(q6(414092133))