# 파일명 및 함수명을 변경하지 마시오.
# 추가 모듈이나 패키지를 import 할 수 없습니다.
def q4(word):
    """
    아래에 코드를 작성하시오.
    word는 소문자로만 구성 되어있습니다.
    word에 등장하는 알파벳을 key로, 갯수를 value로 가지는 딕셔너리를 반환합니다.
    딕셔너리 결과 값만 같으면, 순서는 상관없습니다.
    """
    bin = {}
    for i in word:
        if i not in bin:
            bin[i] = 1
        else:
            bin[i] += 1
    return bin


# 실행 결과를 확인하기 위한 코드입니다. 수정하지 마시오.
if __name__ == '__main__':
    print(q4('hello'))
    print(q4('internationalization'))
    print(q4('haha'))