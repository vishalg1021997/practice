#You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.

def split_and_join(line):
    a = line.split(" ")
    b = ("-").join(a)
    return b

z = input()
print(split_and_join(z))