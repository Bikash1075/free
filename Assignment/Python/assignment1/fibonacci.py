# declare 3 varibles (f0,f1,f2)
# assign values, f0=0, f1=1,f2=0
# for creating fibonacci series
# take input from user
n=int(input("Enter last number "))
f0=0
f1=1
f2=0 #will hold the sum for later during iteration
for i in range(0,n):
    if n<=1:
       print(1)
    
    else:
        f0=f1
        f1=f2
        f2=f0+f1
        print(f2,end=" ")
# fibonacci series upto n given number 
n=int(input("Enter last number "))
f0=0;f1=1;sum=0
while n>sum:
    print(sum,end=" ")
    f0=f1;f1=sum
    sum = f0+f1
    # print(sum,end=" ")



            


        