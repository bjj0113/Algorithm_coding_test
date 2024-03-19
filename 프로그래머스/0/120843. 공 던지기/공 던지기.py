def solution(numbers, k):
    answer = 0
    numbers = numbers * k
    idx = 0
    for i in range(k-1):
        idx += 2
    answer = numbers[idx]
            
    return answer