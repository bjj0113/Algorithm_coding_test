def solution(num, total):
    answer = [0]*num
    if(num%2 == 1):#짝수
        for x in range(num):
            answer[x] = total/num - num//2 + x # 중간값 - 중간값의 인덱스 + x(1씩증가)
    else: #홀수
        for x in range(num):
            answer[x] = total//num - num/2 +1 + x 
    
    return answer