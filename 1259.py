
while True:
    n = str(input())
    if n == "0":
        break
    b = True
    for i in range(len(n)//2):
        if n[i] != n[-i-1]:
            b = False
            break
    if b == True:
        print("yes")
    else:
        print("no")
    

    
    
    