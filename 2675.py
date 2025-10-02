t = int(input())
total = []
for _ in range(t):    
    r, q = input().split()
    r = int(r)
    result = ''
    for i in q:
        result += i*r
    total.append(result)

for k in total:
    print(k)