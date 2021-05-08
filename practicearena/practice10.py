n = int(input())
def Fibonacci(n):
     l =[]
     a = 0
     b = 1
     c = 0
     l.append(a)
     while len(l) != n:
         if n <= 0:
             print("Incorrect input")
         elif n > 0:
             for i in range(0,n):
                 c = b + a
                 a = b
                 b = c
                 l.append(c)
     print(c)
     print(l)
Fibonacci(n)

# a = 0
# b = 1
# c = 0
# for i in range(1, n):
#     print(c)
#     c = b + a
#     a = b
#     b = c
# print(c)
