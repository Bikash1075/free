# Write a Python program to reverse a string.
# ﻿Sample String : "1234abcd"

# Expected Output : "dcba4321"

# 1st approach
def revstring(samplestring):
    return samplestring[::-1]
Sample_String = "1234abcd"
print(revstring(Sample_String))


# def revstring(n):
#     n=n[::-1]
#     return n
# Sample_String = "1234abcd"
# print(revstring(Sample_String))

# 2nd approach
def revstring(n):
    smpstr=''
    for i in n:
        smpstr= i+smpstr
    return smpstr
n="1234abcd"
print(revstring(n))

# 3rd approach
def revstring(n):
    l = list(n)
    l.reverse()
    rstring=''.join(l)
    return rstring
n= "1234abcd"
print(revstring(n))