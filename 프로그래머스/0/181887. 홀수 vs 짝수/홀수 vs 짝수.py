def solution(num_list):
    answer = 0
    odd, even = 0,0
    for i in range(0,len(num_list),2): #odd
        odd = odd + num_list[i]
        
    for i in range(1,len(num_list),2): #even
        even = even + num_list[i]
        
    if odd > even:
        answer = odd
    else:
        answer = even
    return answer