def solution(phone_book):
    short = min(phone_book)
    for i in phone_book:
        if i!=short and short in i:
            return False
            break
    return True