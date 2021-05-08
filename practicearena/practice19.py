x = input()
y = input()
for i in range(int(x),int(y)+1):
    a = str(i)
    if (int(a[0])**3) + (int(a[1])**3) + (int(a[2])**3) == i:
        print(i)


# a = str(x)
# if (int(a[0])**3) + (int(a[1])**3) + (int(a[2])**3) == int(x):
#     print(x)