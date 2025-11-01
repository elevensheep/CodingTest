def func(n, k):
    if k == 0 or n == k:
        return 1
    return func(n-1, k) + func(n-1, k-1)

n, k = map(int, input().split())

print(func(n, k))

