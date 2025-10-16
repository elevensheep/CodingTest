# def solution(scoville, K):
#     answer = 0
#     scoville.sort()

#     while scoville[0] < K:
#         if len(scoville) < 2:
#             return -1
            
#         first = scoville.pop(0)
#         second = scoville.pop(0)
#         total = first + (second * 2)
        
#         scoville.append(total)
#         answer += 1
        
#         scoville.sort() 

#     return answer

# 큐를 이용한 풀이

import heapq

def solution(scoville, k):
    answer = 0
    heapq.heapify(scoville)
    
    while scoville[0] < k and len(scoville) > 1:
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        total = first + (second * 2)
        heapq.heappush(scoville, total)
        answer += 1
    
    if len(scoville) < 2 and scoville[0] < k:
            return -1
    return answer




