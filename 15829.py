def func(n) -> int:
    result = 0
    for i in range(len(n)):
        result += (ord(n[i])-96)* (31**int(i))
    return result % 1234567891

l = int(input())
h = str(input())
if l == len(h):
    print(func(h))