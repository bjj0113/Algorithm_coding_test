import sys
input = sys.stdin.readline

def gcd(a,b):
    while b > 0:
        a,b = b,a % b
    return a

n = int(input())
tree = list()
tree_gap = list()
for _ in range(n):
    x = int(input())
    if tree:
        tree_gap.append(x - tree.pop())
        tree.append(x)
    else:
        tree.append(x)

set_tree_gap = sorted(list(set(tree_gap)))
if len(set_tree_gap)>1:
    min_tree_gap = set_tree_gap[0]
    for i in range(1,len(set_tree_gap)):
        min_tree_gap = gcd(set_tree_gap[i],min_tree_gap)
    cnt = 0
    for t in tree_gap:
        cnt += (t // min_tree_gap) - 1

    print(cnt)
else:
    print(0)
