def solution(brige_length, weight, truck_weights):
    answer=1
    cur_truck=[0]*bridge_lenth
    cur_weight = 0
    while True: 
        cur_weight -=cur_truck.pop(0)
        cur_truck = cur_truck +[0]
        if len(truck_weights) >0 and  cur_weight + truck_weights[0] <= weight:
            cur_truck[-1] = truck_weights.pop(0)
            cur_weight+=cur_truck[-1]
        
        print(cur_truck)
        
        if cur_weight ==0 and len(truck_weights) ==0:break
        answer+=1
        
    return answer

bridge_lenth =2
weight = 10
truck_weights =[7,4,5,6]
print(solution(bridge_lenth,weight,truck_weights))