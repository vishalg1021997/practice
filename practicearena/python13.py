Max_limit_quantity = list(map(int,input().split()))
Prescribed_quantity = list(map(int,input().split()))

def how_many_vaccines(Max_limit_quantity,Prescribed_quantity):
    mx=[]
    for i in range(len(Max_limit_quantity)):
        mx.append(Max_limit_quantity[i]//Prescribed_quantity[i])
        mx.sort()
    print(mx[0])

how_many_vaccines(Max_limit_quantity,Prescribed_quantity)