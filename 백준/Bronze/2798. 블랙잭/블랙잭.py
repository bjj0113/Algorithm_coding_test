def sol(n,m,card):
    closed = float('inf')
    sumx = 0
    for a in range(0,n-2):
        if card[a] < m:
            for b in range(a+1,n-1):
                if card[a]+card[b] < m:
                    for c in range(b+1,n):
                        if card[a]+card[b]+card[c] <= m:
                            if m - (card[a]+card[b]+card[c]) == 0:
                                return card[a]+card[b]+card[c]
                            elif m - (card[a]+card[b]+card[c]) < closed:
                                closed = m - (card[a]+card[b]+card[c])
                                sumx = card[a]+card[b]+card[c]                             
    return sumx

n,m = map(int,input().split())
card =list(map(int,input().split()))
print(sol(n,m,card))