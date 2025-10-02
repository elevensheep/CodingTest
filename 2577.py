a = int(input())
b = int(input())
c = int(input())

arr = str(a * b * c)
result = [0] * 10 
for i in arr:
    result[int(i)] += 1

for i in result:
    print(i)