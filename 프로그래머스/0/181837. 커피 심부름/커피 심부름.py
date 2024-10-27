def solution(order):
    answer = 0
    x = '_'.join(order)
    x = x.replace('anything','americano')
    
    cnt1 = x.count('americano')
    cnt2 = x.count('cafelatte')
    answer = cnt1 * 4500 + cnt2 * 5000
    return answer