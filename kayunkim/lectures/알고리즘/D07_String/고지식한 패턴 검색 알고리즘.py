p = 'is' #찾을 패턴
t = 'This is a book~!' 전체 텍스트
M = len(p)  #찾을 패턴의 길이
N = len(t)  #전체 텍스트의 길이

def BruteForce(p,t):
    i = 0 # t의 인덱스
    j = 0 # p의 인덱스
    while j<M and i<N:      #패턴길이, 전체 텍스트 길이만큼 반복
        if t[i] != p[j]:
            i = i - j
            j = -1
        i = i +1
        j = j +1
    if j == M :