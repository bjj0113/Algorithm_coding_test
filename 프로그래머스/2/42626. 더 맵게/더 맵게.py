import heapq
def solution(scoville, K):
    answer = 0 
    heapq.heapify(scoville)
    
    while 1 :
        x1 = heapq.heappop(scoville)
        if x1 >= K:
            break
        if x1 < K and len(scoville) == 0:
            answer = -1
            break
        x2 = heapq.heappop(scoville)

        new = x1 + x2+x2

        heapq.heappush(scoville, new)
        answer += 1
    return answer