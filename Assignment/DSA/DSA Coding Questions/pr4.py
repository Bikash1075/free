# Given an array arr[] of integers. Find a peak element i.e. 
# an element that is not smaller than its neighbors. 

# Note: For corner elements, we need to consider only one neighbor. 

# Example:

# Input: array[]= {5, 10, 20, 15}

# Output: 20

# Explanation: The element 20 has neighbors 10 and 15, 
# both of them are less than 20.

# Input: array[] = {10, 20, 15, 2, 23, 90, 67}

# Output: 20 or 90

# Explanation: The element 20 has neighbors 10 and 15, 
# both of them are less than 20, similarly 90 has 
# neighbors 23 and 67.
# 1st approach
def peak_element(arr,n):
    for i in range(n):
        if (arr[i] > arr[i - 1] and arr[i] > arr[i + 1]) :
            return arr[i]
arr=[10, 20, 15, 2, 23, 90, 67]
n = len(arr)
print(peak_element(arr,n))
# 2nd approach
def peak_element(arr,n):
    for i in range(n-1,0,-1):
        if (arr[i] > arr[i - 1] and arr[i] > arr[i + 1]) :
            return arr[i]
arr=[10, 20, 15, 2, 23, 90, 67]
n = len(arr)
print(peak_element(arr,n))

# 3rd approach
def peak_element(arr,n):
    for i in range(1,n-1):
        if arr[i-1]<arr[i] and arr[i+1]<arr[i]:
            print(arr[i])
arr=[10, 20, 15, 2, 23, 90, 67]
n=len(arr)
peak_element(arr,n)


# 3rd approach
arr = [10, 20, 15, 2, 23, 90, 67]
def peak_element(arr,n):
    for i in range(1,n-1):
        if arr[i]>arr[i-1]:
            if arr[i]==arr[n-1]:
                pass
            elif arr[i]>arr[i+1]:
                print(arr[i])
arr=[10, 20, 15, 2, 23, 90, 67]
n=len(arr)
peak_element(arr,n)


def peak_element(arr,n):
    for i in range(n):
        if (arr[i] > arr[i - 1] and arr[i] > arr[i + 1]) :
            return arr[i]
arr=[10, 20, 15, 2, 23, 90, 67]
n = len(arr)
print(peak_element(arr,n))