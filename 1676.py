def factorial(n) -> int:
    if n == 0:
        return 1
    return n * factorial(n-1)

n = int(input())
num = factorial(n)
num = list(str(num))
count = 0

while num:
    if '0' not in num:
        break
    
    zero = num.pop()

    if zero != '0':
        break
    else:
        count += 1

print(count)
