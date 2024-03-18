def solution(num_list, n):
    answer = []
    a = 0
    for x in range(len(num_list)//n):
        answer.append([])
        for y in range(n):
            answer[x].append(num_list[a])
            a += 1
            
    return answer