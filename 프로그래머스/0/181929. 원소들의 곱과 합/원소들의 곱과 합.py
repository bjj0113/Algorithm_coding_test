def solution(num_list):
    answer = 0
    sumi =0
    muli=1
    for i in num_list:
        sumi+= i
        muli*=i
    if muli<sumi*sumi:
        answer =1
    else:
        answer=0
    return answer