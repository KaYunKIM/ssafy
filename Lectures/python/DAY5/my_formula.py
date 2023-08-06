def my_max(a,b):
    if a >b:
        print(f'{a}가 더 큽니다!')
    else:
        print(f'{a}가 더 큽니다!')

print('여기는 무조건 실행됩니다.')

if __name__=='__main__':
    print('직접 실행한 경우만 실행됩니다.')
    print(__name__)
    my_max(3,5)