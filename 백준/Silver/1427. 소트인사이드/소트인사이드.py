
n = input()
li = list()
for x in n:
    li.append(int(x))
        
print("".join(map(str,sorted(li,reverse = True))))