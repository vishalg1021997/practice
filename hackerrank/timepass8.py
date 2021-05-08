# Mr.Vincent works in a door mat manufacturing company.One day, he designed a new door mat with the
# following specifications
# Mat size must be N X.M (N is an odd natural number, and M is 3 times .)
# The design should have 'WELCOME' written in the center.
# The design pattern should only use |, . and - characters.
#
# Sample Designs
#
# Size: 7 x 21
#
# ---------.|.---------
# ------.|..|..|.------
# ---.|..|..|..|..|.---
# -------WELCOME - ------
# ---.|..|..|..|..|.---
# ------.|..|..|.------
# ---------.|.---------
#
# Size: 11 x 33
#
# ---------------.|.---------------
# ------------.|..|..|.------------
# ---------.|..|..|..|..|.---------
# ------.|..|..|..|..|..|..|.------
# ---.|..|..|..|..|..|..|..|..|.---
# -------------WELCOME - ------------
# ---.|..|..|..|..|..|..|..|..|.---
# ------.|..|..|..|..|..|..|.------
# ---------.|..|..|..|..|.---------
# ------------.|..|..|.------------
# ---------------.|.---------------

n, m = input().split(" ")
if int(n)%2!=0 and int(m) == int(n) * 3:
    for i in range(1, int(n)+1):
        print(('.|.'*((i*2)-1)).center(int(m), '-'))
        if (int(n)//2) == i:
            print("WELCOME".center(int(m), '-'))
            for j in reversed(range(1,i+1)):
                print(('.|.' * ((j * 2) - 1)).center(int(m), '-'))
            break

