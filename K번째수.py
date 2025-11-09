def solution(array, commands):
    answer = []
    for command in commands:
        start = command[0] - 1
        end = command[1]
        k = command[2] - 1
        arr = array[start:end]
        arr.sort()
        num = arr[k]
        answer.append(num)
        
    return answer