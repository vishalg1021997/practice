n = int(input())
l = []
for i in range(n):
    a = input()
    l.append(a)
print(sorted(l, key = lambda  x : x[len(x)-2]))