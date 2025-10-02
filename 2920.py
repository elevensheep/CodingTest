arr = list(map(int, input().split()))
result = ""

if arr[0] == 1:
    for i in range(8):
        if arr[i] != i + 1:
            result = "mixed"
            break
    else: 
        result = "ascending"
elif arr[0] == 8:
    for i in range(8):
        if arr[i] != 8 - i: 
            result = "mixed"
            break
    else: 
        result = "descending"
else:
    result = "mixed"

print(result)