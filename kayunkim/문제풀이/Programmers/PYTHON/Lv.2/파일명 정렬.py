def solution(files):
    temp = []
    cap = [0]*len(files)
    for file in files:
        H = ''
        N = ''
        T = ''
        
        for i in file:
            if i.isdigit():
                N+=i
            else:
                if N:
                    T+=i
                else:
                    if i.isupper():
                        if not cap[files.index(file)]:
                            cap[files.index(file)] = 1
                    H+=i        

        if T.isspace():
            temp.append([H,N])
        else:
            temp.append([H,N,T])
    
    if 0 in cap:
        for c in range(len(cap)):
            if cap[c]:
                temp[c].append([temp[c][0], 0])
                temp[c][0] = temp[c][0].lower()

    temp = sorted(temp, key=lambda x: (x[0], int(x[1])))
    
    for t in temp:
        if type(t[-1]) == list:
            t[0] = t[-1][0]
            t.pop()
        if not t[-1]:
            t.pop()
    
    return [''.join(i) for i in temp]





    def solution(files):
    temp = []
    cap = [0]*len(files)
    for file in files:
        H = ''
        N = ''
        T = ''
        
        for i in file:
            if i.isdigit():
                N+=i
            else:
                if N:
                    T+=i
                else:
                    H+=i        
        temp.append([H,N,T])

    temp = sorted(temp, key=lambda x: (x[0].lower(), int(x[1])))
    
    return [''.join(i) for i in temp]



import re

def solution(files):
    temp = [re.split(r"([0-9]+)" ,file) for file in files]
    ans = sorted(temp, key=lambda x: (x[0].lower(), int(x[1])))
    
    return [''.join(i) for i in ans]