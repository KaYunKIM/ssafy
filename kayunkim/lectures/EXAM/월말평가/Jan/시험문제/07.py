# 파일명 및 함수명을 변경하지 마시오.
# 추가 모듈이나 패키지를 import 할 수 없습니다.
def q7(n):
    """
    아래에 코드를 작성하시오.
    n은 9이하의 양의 정수이다.
    n을 바탕으로 가능한 암호의 갯수를 정수로 반환합니다.
    """
    number = [0,1,2,3,4,5]
    ans = [0]*3
    bin = []
    for i in number:
        if n-i in number:
            bin[0] = i
            bin[2] = n-i
        if i != bin[0] and i != bin[2]:
            bin[1] = i
        return ans





# 실행 결과를 확인하기 위한 코드입니다. 수정하지 마시오.
if __name__ == '__main__':
    print(q7(9))
    print(q7(4))