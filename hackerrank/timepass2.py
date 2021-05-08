n = int(input())
arr = map(int, input().split())
l = list(arr)[:n]
a = max(l)
while max(l)==a:
    l.remove(max(l))
print(max(l))
