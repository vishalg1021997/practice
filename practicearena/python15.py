n = int(input())
l = []
for i in range(n):
    a,b = input().split()
    c = (a,int(b))
    l.append(c)
print(sorted(l, key = lambda x: int(x[1])))
