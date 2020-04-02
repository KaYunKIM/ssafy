A = []

def subset(k,N):
    if k==N:
        return
    else:
        A.append(arr[k])
        subset(k+1,N)
        A.pop()
        bit[k]=0
        subset(k+1,N)
