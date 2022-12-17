# Q4. Write a program to print the first non-repeated character from a string?

def first_non_repeated_char(string):
    arr=[]
    n_arr=[]
    for i in range (len(string)):
        arr.append(string[i])
    for i in range (len(arr)):
        if arr.count(arr[i])==1:
            n_arr.append(arr[i])
    return n_arr[0]
    
string = input("Enter your string ")
print(first_non_repeated_char(string))

