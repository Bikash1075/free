# Q2. Write a program to reverse an array in place? 
# In place means you cannot create a new array. 
# You have to update the original array.
def rev_arr(arr,n):
    for i in range(n-n//2):
        arr[i],arr[n-i-1]=arr[n-i-1],arr[i]
    print(arr)
arr=[1,2,3,4,5]
n=len(arr)
rev_arr(arr,n)

def rev_arr(arr,n):
    for i in range(n//2):
        arr[i],arr[n-i-1]=arr[n-i-1],arr[i]
    print(arr)
arr=[1,2,3,4,5]
n=len(arr)
rev_arr(arr,n)

# 2nd approach
def rev_arr(arr,start,end):
    n=len(arr)
    for i in range(n):
        if start<end:
            arr[start],arr[end]=arr[end],arr[start]
        start=start+1
        end=end-1 
arr=[14,25,87,69,36]
start=0;end=len(arr)-1
rev_arr(arr,start,end)
print(arr)

# 3rd approach
def rev_arr(arr,start,end):
    while start<end:
        arr[start],arr[end]=arr[end],arr[start]
        start=start+1
        end=end-1 
arr=[14,25,87,69,36]
start=0;end=len(arr)-1
rev_arr(arr,start,end)
print(arr)
