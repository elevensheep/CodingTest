from re import match

def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)):
        for k in range(i+1,len(phone_book)):
            if match(phone_book[i], phone_book[k]):
                answer = False
            
    return answer

phone_book = ["119", "97674223", "1195524421"]
print(solution(phone_book))