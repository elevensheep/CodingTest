while(1):
    a, b, c = map(int,input().split)
    if(a**2+b**2 == c**2):
        print("right")
    elif(a == 0 and b == 0 and c == 0):
        break
    else:
        print("wrong")