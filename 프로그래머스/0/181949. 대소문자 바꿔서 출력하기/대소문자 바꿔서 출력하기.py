str = input()

x = list(str)
a = []
for k in str:
    if k.isupper():
        a.append(k.lower())
    else:
        a.append(k.upper())

answer = ''.join(a)
print(answer)