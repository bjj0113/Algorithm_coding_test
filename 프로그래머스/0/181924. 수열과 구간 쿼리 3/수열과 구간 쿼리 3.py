def solution(arr, queries):
    #answer = []
    for i,k in enumerate(queries):
        arr[k[0]], arr[k[1]] = arr[k[1]], arr[k[0]]
    return arr