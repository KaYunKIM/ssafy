def solution(phone_number):
    ans = list('*'*len(phone_number))
    ans[-4:len(phone_number)] = phone_number[-4:len(phone_number)]
    return ''.join(map(str,ans))