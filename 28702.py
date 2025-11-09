def numToStr(num):
    num = int(num)
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return str(num)
    
# arr = []
# for  _ in range(3):
#     n = input()
#     arr.append(n)

# for i in range(len(arr)):
#     if arr[i] 
print(type('str') == str)