# Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Upper case characters : 3
# No. of Lower case Characters : 12

# 1st approach
def count_upper_lower(n):
    c_upper=0
    c_lower=0
    for i in n:
        if ord(i)<=90 and ord(i)>=65:
            c_upper= c_upper+1
        elif ord(i)<=122 and ord(i)>=97:
            c_lower= c_lower+1
    print("No. of Upper case characters :",c_upper)
    print("No. of Lower case characters :",c_lower)
    return ''
n=input("Enter a string ")
print(count_upper_lower(n))

# 2nd approach
def count_upper_lower():
    n=input("Enter a String ")
    Ucount=0
    Lcount=0
    for i in n:
       if i.isupper():
            Ucount=Ucount+1
       elif i.islower():
            Lcount=Lcount+1
    print("No. of Upper case characters :",Ucount)
    print("No. of Lower case characters :",Lcount)
    return ''
print(count_upper_lower())

# 3rd approach
def count_upper_lower():
    n=input("Enter a String ")
    l1=[]
    l2=[]
    for i in n:
        if i.isupper():
            l1.append(i)
            luc=len(l1)
        elif i.islower():
            l2.append(i)
            llc=len(l2)
    print("No. of Upper case characters :",luc)
    print("No. of Lower case characters :",llc)
    return ''
print(count_upper_lower())
