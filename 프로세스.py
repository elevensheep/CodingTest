def solution(priorities, location):
    answer = 0
    priorities = [(p, i) for i, p in enumerate(priorities)]
    print(priorities)
    while True:
        head = priorities.pop(0)
        if any(head[0] < index[0] for index in priorities):
            priorities.append(head)
        else:
            answer += 1
            if head[1] == location:
                return answer
                    