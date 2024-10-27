def solution(rank, attendance):
    answer = 0
    x = list(zip(rank,attendance))
    y = sorted(x)
    at = []
    for i,j in y:
        if j is True:
            at.append(i)
    answer = 10000 * rank.index(at[0]) + 100 * rank.index(at[1]) + rank.index(at[2])
    return answer