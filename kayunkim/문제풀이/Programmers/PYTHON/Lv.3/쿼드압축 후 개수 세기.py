def solution(arr):
    def check(y, x, n):
        if n == 1:
            if arr[y][x] == 1:
                return [0, 1]
            else:
                return [1,0]
        
        first = check(y, x, n // 2)
        sec = check(y, x + n//2, n//2)
        third = check(y+n//2, x, n//2)
        fourth = check(y + n//2, x + n//2, n//2)
    
        if first == sec == third == fourth == [0,1] or first == sec == third == fourth == [1,0]:
            return first
        else:
            return list(map(sum, zip(first, sec, fourth, third))

    ans = check(0,0,len(arr))
    return ans