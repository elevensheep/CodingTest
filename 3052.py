arr = []
for _ in range(10):
    a = int(input()) % 42
    arr.append(a)

arr = set(arr)
print(len(arr))