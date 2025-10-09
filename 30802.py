import math

n = int(input())
arr = list(map(int, input().split()))
t, p = map(int, input().split())
count = 0
total = 0
for i in arr:
    total += i

if n == total:
    for i in arr:
        count += math.ceil(float(i)/t)
    print(count)
    print(int(n/p), end=" ")
    print(n % p, end=" ")

else:
    Exception 