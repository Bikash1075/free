def rev_arr(arr,n):
    for i in range(2):
        arr[i],arr[n-i-1]=arr[n-i-1],arr[i]
    print(arr)
arr=[14,25,87,69,36,55,41,69,84,53]
n=len(arr)
rev_arr(arr,n)