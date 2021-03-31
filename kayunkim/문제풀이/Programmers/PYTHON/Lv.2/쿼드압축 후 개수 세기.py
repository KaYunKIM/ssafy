def solution(arr):
    answer = [0,0]
    for a in range(len(arr)):
        for i in range(len(arr)):
            h = 2
            while i+h<=len(arr):
                one = 0
                zero = 0
                temp = []

                for j in range(h):
                    if 2 not in arr[j][i:i+h]:
                        temp.append(arr[j][i:i+h])
                        one+=arr[j][i:i+h].count(1)
                        zero+=arr[j][i:i+h].count(0)

                if zero == h*2:
                    answer[0]+=1
                    for t in temp:
                        t = [2]*h

                elif one == h*2:
                    answer[1]+=1
                    for t in temp:
                        t = [2]*h

                h+=1
    return answer

    answer = 0
    left = 1
    right = max(times)*n

    while left <= right:
        mid = (left+right)//2
        cnt = 0

        for i in times:
            cnt += mid//i
            if cnt >= n:
                break

        if cnt >= n:
            answer = mid
            right = mid-1

        else:
            left = mid+1