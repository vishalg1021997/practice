n = int(input())
a = 0

while (len(a) != 1):
    for i in str(n):
        a = a + int(i)
        # if len(a) != 1:

print(a)