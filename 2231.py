n = int(input())
result = 0
for i in range(1,n+1):
    num = str(i)
    total = 0
    for k in num:
        total += int(k)
    total += i
    if total == n:
        result = i
        break    
print(result)
