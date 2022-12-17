# Write a Python Program to print full pyramid using '*' symbol. The pattern should be as shown below:

# *

# * * *

# * * * * *

# * * * * * * *

# * * * * * * * * *

def triangle(n):
    for i in range(1,n+1):
        for j in range(1,2*i):
            print('*', end=' ')
        print()
        print()
n=5
triangle(n)
# solution2
def triangle2(n):
    for i in range(0,n):
        print('* '*(2*i+1))
        print()
n=5
triangle2(n) 

#3rd approach
def triangle3(n):
    for i in range(1,n+1):
        print('* '*(2*i-1))
        print()
n=5
triangle3(n) 