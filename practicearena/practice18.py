l = list(map(int, input().split()))
value = int(input())
cont = 0
for i in l:
    for j in l:
        for k in l:
            if i + j + k == value:
                cont = cont + 1
print(cont)