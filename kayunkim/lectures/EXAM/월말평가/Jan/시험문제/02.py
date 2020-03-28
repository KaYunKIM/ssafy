# 파일명 및 함수명을 변경하지 마시오.
# 추가 모듈이나 패키지를 import 할 수 없습니다.
def q2(word):
    """
    아래에 코드를 작성하시오.
    word는 소문자로만 구성 되어있습니다.
    word에 있는 모음의 갯수를 정수로 반환합니다.
    """

    vowels = 'aeiou'
    cnt = 0
    for i in word:
        if i in vowels:
            cnt+=1
    return cnt



# 실행 결과를 확인하기 위한 코드입니다. 수정하지 마시오.
if __name__ == '__main__':
    print(q2('hello'))
    print(q2('internationalization'))
    print(q2('ssafy'))