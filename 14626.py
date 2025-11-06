def func(isbn):
    total = 0
    err_index = 0  
    
    for i in range(len(isbn)):
        
        char = isbn[i] 
        if(i % 2 == 1): 
            if(char == '*'):
                err_index = 3
                continue
            total += 3 * int(char)
        else: 
            if(char == '*'):
                err_index = 1
                continue
            total += int(char)

    remainder = total % 10
    target = (10 - remainder) % 10
    
    for missing_digit in range(10): 
        if (missing_digit * err_index) % 10 == target:
            return missing_digit 
    return -1


isbn = str(input())
result = func(isbn)
print(result)
