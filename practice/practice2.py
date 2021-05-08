n = int(input())
for i in range(1,n+1):
    print(" " * n, end="")
    for j in range(1,i):
        print(j,end = "")
    print(i,end = "")
    for j in reversed(range(1,i)):
        print(j,end="")
    print()
    n = n - 1