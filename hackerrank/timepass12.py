# You are given the firstname and lastname of a person on two different lines. Your task is to read them
# and print the following:
#
# Hello firstname lastname! You just delved into python.
#
# Function Description
#
# Complete the print_full_name function in the editor below.
#
# print_full_name has the following parameters:
#
# string first: the first name
# string last: the last name
# Prints
#
# string: 'Hello firstname lastname! You just delved into python' where firstname and lastname are replaced
# with first and last.

def print_full_name(first, last):
    if len(first) <= 10 and len(last) <= 10:
        print("Hello", first, last.ljust(len(last) + 1, "!"),"You just delved into python.")
        return first, last

firstname = input()
lastname = input()
print_full_name(firstname,lastname)

