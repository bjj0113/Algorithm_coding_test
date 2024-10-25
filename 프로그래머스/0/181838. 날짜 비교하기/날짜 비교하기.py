def solution(date1, date2):
    answer = 0
    list1 = list(zip(date1,date2))
    print(list1)
    for i,k in enumerate(list1):
        if k[0] < k[1]:
            answer = 1
            break
        elif k[0] == k[1]:
            answer = 0
        else:
            answer = 0
            break
    return answer