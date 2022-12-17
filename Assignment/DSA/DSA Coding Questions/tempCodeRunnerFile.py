def peak_element(arr,n):
    for i in range(n-1):
        if (arr[i] > arr[i - 1] and arr[i] > arr[i + 1]) :
            return arr[i]
arr=[10, 20, 15, 2, 23, 90, 67]
n = len(arr)
print(peak_element(arr,n))