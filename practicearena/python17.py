l = list(map(int, input().split()))
l1 = []
while (len(l) != 0):
    for i in l:
        a = max(l)
        l1.append(a)
        l.remove(a)
        if len(l)==0:
            break
        b = min(l)
        l1.append(b)
        l.remove(b)
print(l1)