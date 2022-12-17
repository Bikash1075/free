# Take a number as input from the user. Print the number in reversed order. 
# For example, for input 567, output should be: 765

def reverse_number(num,n):
    rev=0
    for i in range(n):
        rem = num%10
        rev=rev*10+rem
        num=num//10
    print(rev)
num=int(input())
n = len(str(num))
reverse_number(num,n)

# 2nd approach
def reverse_number(num):
    rev=0
    while num!=0:
        rem=num%10
        rev=rev*10+rem
        num=num//10
    print(rev)
num=int(input())
reverse_number(num)

