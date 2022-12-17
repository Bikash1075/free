# Q1. Write a program to find all pairs of an integer array 
# whose sum is equal to a given number?
def pair_of_int(arr,sum):
    n = len(arr)
    for rows in range(n):
        for columns in range(rows+1,n):
            if arr[rows]+arr[columns]==sum:
                pair=arr[rows],arr[columns]
                print (pair,end=' ')
        
arr=[20,35,21,45,-32,10,65,-10,55,87]
sum=55
pair_of_int(arr,sum)

