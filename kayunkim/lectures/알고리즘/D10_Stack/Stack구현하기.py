'''
스택구현하기
구현한 스택을 이용해서 3개의 데이터를 스택에 저장하고 다시 3번 꺼내서 출력하기
'''

#크기가 정해진 리스트를 사용해서 스택구현
stack = [0]*10
top = -1
#push연산 : top을 하나 늘리고, stack의 top인덱스에 원소를 삽입
#push(1)
top +=1
stack[top] = 1
#push(2)
top += 1
stack[top] = 2
#push(3)
top+=1
stack[top] = 3
#pop연산 : top인덱스 원소 리턴(출력)하고 top을 하나 줄임
# r = stack[top]
# top -= 1
# print(r)
# print(top)
#
# #모든 원소 꺼내기 : 스택이 비어있지 않으면 스택의 원소를 꺼내 리턴(출력)
# while top != -1:
#     r = stack[pop]
#     top-= 1
#     print(r, end=' ')

#리스트 기능 이용해서 스택 구현하기
s = list()
#push : list의 append
s.append(10)
s.append(20)
s.append(30)
print(s)

#스택의 모든 원소 꺼내서 출력하기
while len(s) != 0:
    print(s.pop(), end=' ')