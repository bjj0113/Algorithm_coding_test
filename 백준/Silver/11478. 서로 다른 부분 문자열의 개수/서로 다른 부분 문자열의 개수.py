import sys
input = sys.stdin.readline

s = input().strip()
Sset = set()
for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        Sset.add(s[i:j])
        
print(len(Sset))
            