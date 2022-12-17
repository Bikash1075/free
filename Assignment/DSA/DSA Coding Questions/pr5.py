# Given an array, cyclically rotate the array clockwise by one. 

# Examples:  

# Input: arr[] = {1, 2, 3, 4, 5}

# Output: arr[] = {5, 1, 2, 3, 4}
def rotation(arr,n):
    x=arr[n-1]
    for i in range(n-1,0,-1):
        arr[i]=arr[i-1]
    arr[0]=x
    return arr
arr=[254,47,15,69,58,41]
n= len(arr)
print(rotation(arr,n))

# 2nd approach
def circularlly_rotated(arr,n):
    temp=[]
    for i in range(n):
        temp.append(arr[i - 1])
    arr=temp[:]
    return arr
arr=[20,50,47,89,56,23]
n= len(arr)
print(circularlly_rotated(arr,n))

def rotate(arr,n):
    a=arr[n-1]
    for i in range(n-1,0,-1):
        arr[i]=arr[i-1]
    arr[0]=a
    return arr
arr=[1,2,3,4,5]
n=len(arr)
print(rotate(arr,n))

def rotate_by_one(arr,n):
    a=arr[n-1]
    for i in range(n-1,0,-1):
        arr[i]=arr[i-1]
    arr[0]=a
    print (arr)
arr=[25,78,45,15,48,79,46]
n= len(arr)
rotate_by_one(arr,n)

def rotate_by_one(arr,n):
    a=arr[n-1]
    for i in range(n-1,0,-1):
        arr[i]=arr[i-1]
    arr[0]=a
    print (arr)
arr=[25,78,45,15,48,79,46]
n= len(arr)
rotate_by_one(arr,n)