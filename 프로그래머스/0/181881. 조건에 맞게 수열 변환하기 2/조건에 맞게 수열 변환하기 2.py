def solution(arr):
    cnt = 0
    while 1:
        next_arr = []
        for k in arr:
            if k>= 50 and k%2 == 0:
                next_arr.append(k//2)
            elif k< 50 and k%2 == 1:
                next_arr.append(k*2 +1)
            else:
                next_arr.append(k)
            
        if next_arr == arr:
            break
        cnt += 1
        arr = next_arr
    return cnt