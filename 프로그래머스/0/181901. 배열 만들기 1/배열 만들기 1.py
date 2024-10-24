def solution(n, k):
    answer = []
    i = 1
    x = 0
    while x < n:
        x = k *i
        if x > n:
            break
        answer.append(x)
        i = i +1
    return answer