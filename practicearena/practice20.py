n = int(input())

for i in range(1,n+1):
    print("."*i)
    if i == n:
        for j in reversed(range(i)):
            print("."*j)