# Given an array of integers, find the length of the longest sub-sequence such that elements in the subsequence are consecutive integers, the consecutive numbers can be in any order. 

# Examples:  

# Input: arr[] = {1, 9, 3, 10, 4, 20, 2}

# Output: 4

# Explanation: The subsequence 1, 3, 4, 2 is the longest subsequence of consecutive elements

# Input: arr[] = {36, 41, 56, 35, 44, 33, 34, 92, 43, 32, 42}

# Output: 5

# Explanation: The subsequence 36, 35, 33, 34, 32 is the longest subsequence of consecutive elements.

# 1st approach
def long_run(arr,n):
    seq=[]
    arr.sort()
    for i in range (1,n):
        if arr[i]-arr[i-1] ==1:
            seq.append(arr[i])
            seq.append(arr[i-1])
        else:
            break
    print(len(set(seq)))
arr=[36, 41, 56, 35, 44, 33, 34, 92, 43, 32, 42]
n = len(arr)
long_run(arr,n)

# 2nd approach
def long_run(arr,n):
    seq=[]
    arr.sort()
    for i in range (1,n):
        if arr[i-1]-arr[i] ==-1:
            seq.append(arr[i])
            seq.append(arr[i-1])
        else:
            break
    print(len(set(seq)))
arr=[36, 41, 56, 35, 44, 33, 34, 92, 43, 32, 42]
n = len(arr)
long_run(arr,n)

def long_run(arr,n):
    seq=[]
    arr.sort()
    for i in range (n):
        if arr[i+1]-arr[i] ==1:
            seq.append(arr[i])
            seq.append(arr[i+1])
        else:
            break
    print(len(set(seq)))
arr=[36, 41, 56, 35, 44, 33, 34, 92, 43, 32, 42]
n = len(arr)
long_run(arr,n)

# 3rd approach
def logest_subsequence(arr,n):
    arr.sort()
    seq = []
    for i in range(1,n):
        if  0<arr[i]-arr[i-1]<3:
            seq.append(arr[i-1])
            seq.append(arr[i])
        else:
            break
    print(len(set(seq)))
arr = [36, 41, 56, 35, 44, 33, 34, 92, 43, 32, 42]
n=len(arr)
logest_subsequence(arr,n)

# 4th approach
def long_run(arr,n):
    seq=[]
    arr.sort()
    count=0
    for i in range (n):
        if arr[i+1]-arr[i] ==1:
            seq.append(arr[i])
            seq.append(arr[i+1])
        else:
            break
    for  i in range(len(set(seq))):
        count=count+1
    return(count),set(seq)
arr=[36, 41, 56, 35, 44, 33, 34, 92, 43, 32, 42]
n = len(arr)
print(long_run(arr,n))