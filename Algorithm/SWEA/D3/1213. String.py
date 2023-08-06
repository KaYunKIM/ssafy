for tc in range(1,11):
    T = int(input())
    word = input()
    sentence = input()
    ans = sentence.count(word)
    print('#{} {}'.format(tc,ans))

# for tc in range(1,11):
#     T = int(input())
#     word = input()
#     sentence = input()
#     cnt = 0
#     for i in range(len(sentence)-len(word)+1):
#         if sentence[i:i+len(word)] == word:
#             cnt+=1
#     print('#{} {}'.format(tc,cnt))