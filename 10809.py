word = str(input())
arr = [-1] * 26
count = 0

for w in word:
    index = ord(w) - ord('a')
    if arr[index] == -1:
        arr[index] = count
    count += 1

for i in arr:
    print(i, end=" ")