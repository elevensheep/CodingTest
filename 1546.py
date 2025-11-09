def func(arr):
    lst = [i/max(arr) * 100 for i in arr]
    return sum(lst)/len(lst)

n = int(input())
arr = list(map(int, input().split()))

if len(arr) == n:
    print(func(arr))
