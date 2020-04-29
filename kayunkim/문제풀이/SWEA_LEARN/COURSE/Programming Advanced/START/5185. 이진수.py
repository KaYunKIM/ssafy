T = int(input())                 
for tc in range(1,T+1):          
    N, lst = input().split()     
    ans = ''                     
    for i in range(int(N)):      
        num = int(lst[i],16)     
        bin = '000'              
        bin+= format(num,'b')    
        ans+=bin[-4:]            
    print('#{} {}'.format(tc,ans)