# Write a Python Program to print half pyramid using alphabets. 
# The pattern should be as shown below:

# A

# B B

# C C C

# D D D D

# E E E E E

# 1st approach
def triangle(s,n):
    for i in range(n):
        for j in range(0,i+1):
            print(s[i],end=' ')
        print()
        print()
s='ABCDE'
n=len(s)
triangle(s,n)

# 2nd approach
def triangle(n):
    k=65
    for i in range(0,n):
        for j in range(i+1):
            print(chr(i+k),end=' ')
        print()
        print()
triangle(5)

# 3rd approach
def triangle(n):
    for i in range(65,70):
        for j in range(65,i+1):
            print(chr(i),end=' ')
        print()
        print()
triangle(5)

# 4th approach
n,k=5,65
for i in range(0,n):
    print((chr(k+i)+' ')*(i+1))
    print()
