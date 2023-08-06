def sub(i,n):
    global cnt
    if i == n:
        cnt+=1
    else:
        sub(i + 1, n)
        sub(i + 1, n)
    return cnt

cnt = 0
print(sub(0,3))