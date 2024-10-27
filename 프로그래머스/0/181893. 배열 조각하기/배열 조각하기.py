def solution(arr, query):

    for i,k in enumerate(query):
        if i%2==0:
            arr = arr[:query[i]+1]
        elif i%2==1:
            arr = arr[query[i]:]
    return arr