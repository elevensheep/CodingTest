def solution(bridge_length, weight, truck_weights):
    answer = 0
    current = [0] * bridge_length 
    total_weight = 0 

    while current: 
        answer += 1
        
        finished_truck = current.pop(0)
        total_weight -= finished_truck

        if truck_weights: 
            if total_weight + truck_weights[0] <= weight:
                new_truck = truck_weights.pop(0)
                current.append(new_truck)
                total_weight += new_truck
            else:
                current.append(0)
                
    return answer