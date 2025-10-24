t = int(input())

for _ in range(t): 
    k = int(input())
    n = int(input())
    lst = [[0] * (n + 1) for _ in range(k + 1)]

    for i in range(1, n + 1):
        lst[0][i] = i
    
    for i in range(1, k + 1):
        for j in range(1, n + 1):
            lst[i][j] = lst[i][j - 1] + lst[i - 1][j]
    
    print(lst[k][n])