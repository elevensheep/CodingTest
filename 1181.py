import sys

t = int(sys.stdin.readline())
arr = []

for _ in range(t):
    arr.append(sys.stdin.readline().strip())

arr = list(set(arr))
arr.sort(key=lambda x: (len(x), x))

for i in arr:
    print(i)