# Given an integer, n , print the following values for each integer i from 1 to n:
#
# Decimal
# Octal
# Hexadecimal (capitalized)
# Binary

def print_formatted(n):
    for i in range(1, n+1):
        print(i, end = ' ')
    print(" ")
    for i in range(1, n + 1):
        a = hex(i).replace('0x', ' ')
        print(a, end = ' ')
    print(" ")
    for i in range(1, n+1):
         b = oct(i).replace('0', ' ')
         print(b, end = ' ')
    print(" ")
    for i in range(1, n+1):
        c = bin(i).replace('0b', ' ')
        print(c, end = ' ')

z = int(input())
print_formatted(z)
