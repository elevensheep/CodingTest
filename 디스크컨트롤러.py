import heapq

def solution(jobs):
    # 1. 초기화
    num_jobs = len(jobs)
    answer = 0
    current_time = 0  # 현재 시각
    processed_count = 0 # 처리한 작업 수
    
    # 2. 작업을 요청 시간 순으로 정렬
    jobs.sort()
    
    # 3. 현재 처리 가능한 작업을 담을 최소 힙(대기 큐)
    # (소요 시간, 요청 시간) 순서로 넣어야 소요 시간 기준으로 정렬됩니다.
    ready_queue = []
    
    job_index = 0 # jobs 리스트를 순회할 인덱스

    # 4. 모든 작업이 처리될 때까지 반복
    while processed_count < num_jobs:
        
        # 5. 현재 시점(current_time)까지 요청된 모든 작업을 힙에 추가
        while job_index < num_jobs and jobs[job_index][0] <= current_time:
            request_time, duration = jobs[job_index]
            heapq.heappush(ready_queue, (duration, request_time))
            job_index += 1
            
        # 6. 대기 큐에 작업이 있는 경우
        if ready_queue:
            # 7. 가장 소요 시간이 짧은 작업을 꺼내서 처리
            duration, request_time = heapq.heappop(ready_queue)
            
            # 작업이 끝난 시점으로 현재 시각 업데이트
            current_time += duration
            
            # 총 소요 시간 계산 (작업 종료 시각 - 요청 시각)
            answer += current_time - request_time
            
            processed_count += 1
        
        # 8. 대기 큐가 비어있는 경우 (디스크가 쉬고 있음)
        #    -> 다음 작업의 요청 시간으로 현재 시각을 점프시킴
        else:
            current_time = jobs[job_index][0]
            
    # 9. 평균 소요 시간 계산
    return answer // num_jobs

# 예시
jobs = [[0, 3], [1, 9], [2, 6]]
print(solution(jobs))  # 결과: 9