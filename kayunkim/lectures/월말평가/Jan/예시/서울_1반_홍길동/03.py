# 파일명 및 함수명을 변경하지 마시오.
# 추가 모듈이나 패키지를 import 할 수 없습니다.
def q3(fruits, add, n):
    """
    아래에 코드를 작성하시오.
    fruits는 현재 과일가게에 현황을 나타내는 딕셔너리입니다.
    add, n은 각각 추가적으로 더해지는 과일과 갯수입니다.
    add, n을 반영한 fruits 딕셔너리를 반환하세요.
    딕셔너리 결과 값만 같으면, 순서는 상관없습니다.
    """

    if add in fruits.keys():
        fruits[add] += n
    else:
        fruits[add] = n
    return fruits
    

# 실행 결과를 확인하기 위한 코드입니다. 수정하지 마시오.
if __name__ == '__main__':
    print(q3({'apple': 1}, 'apple', 3))
    print(q3({'apple': 1}, 'banana', 1))
    print(q3({}, 'apple', 3))