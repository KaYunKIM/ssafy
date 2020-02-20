# 파일명 및 함수명을 변경하지 마시오.
# 추가 모듈이나 패키지를 import 할 수 없습니다.
def q7(n):


    number = [0, 1, 2, 3, 4, 5]
    count = 0
    for i in range(100, 1000):
        if int(str(i)[0]) + int(str(i)[2]) == n and int(str(i)[0]) != int(str(i)[2]) :
            if int(str(i)[0]) in number :
                if int(str(i)[2]) in number :
                    if int(str(i)[1]) in number and int(str(i)[1]) != int(str(i)[0]) and int(str(i)[1]) != int(str(i)[2]):
                        count += 1          

    return count





# 실행 결과를 확인하기 위한 코드입니다. 수정하지 마시오.
if __name__ == '__main__':
    print(q7(9))
    print(q7(4))