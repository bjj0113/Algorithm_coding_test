def solution(my_string, n):
    answer = ''
    for x in range(len(my_string)):
        for y in range(n):
            answer = answer+my_string[x]
    return answer