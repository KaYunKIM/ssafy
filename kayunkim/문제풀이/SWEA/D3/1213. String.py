for tc in range(1,11):
    T = int(input())
    word = input()
    sentence = input()
    ans = sentence.count(word)
    print('#{} {}'.format(tc,ans))