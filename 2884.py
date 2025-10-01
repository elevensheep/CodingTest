h, m = map(int, input().split())

m -= 45
if(m < 0 and h >= 1):
    h -= 1
    m = 60 + m
elif(m < 0 and h == 0):
    h = 23
    m = 60 + m

print(h,m)