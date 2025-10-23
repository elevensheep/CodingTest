n, m = map(int, input().split())

num_max = max(n, m)
num_min = min(n, m)

k = 0
j = 0 

for i in range(1, num_min + 1):
    if num_min % i == 0 and num_max % i == 0:
        k = i 

j = (n * m) // k

print(k) 
print(j) 