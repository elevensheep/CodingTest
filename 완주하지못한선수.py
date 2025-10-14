from collections import Counter

def solution(participant, completion):
    answer = ""
    participantCounter = Counter(participant)
    completionCounter = Counter(completion)
    answer = participantCounter - completionCounter
    return list(answer.keys()).pop()

m, n = ["leo", "kiki", "eden"], ["eden", "kiki"]
print(solution(m,n))