n = int(input())
arr = list(map(int, input().split()))
count = 0

for i in arr:
    if ( i < 2):
        continue
    else:    
        b = True
        for k in range(2,i):
            if (i % k == 0 and i != 0 and k != i):
                b = False
                break
    
        if b == True:
            count += 1

print(count)
