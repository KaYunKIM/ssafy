def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        x= '{0:b}'.format(arr1[i])
        y= '{0:b}'.format(arr2[i])
        ans = ''
        while len(x)!=n or len(y)!=n:
            if len(x) != n:
                x= '0'+x
            if len(y) !=n:
                y = '0'+y
        for j in range(n):
            if x[j] =='1' or y[j]=='1':
                ans+='#'
            else:
                ans+=' '
        answer.append(ans)
    return answer