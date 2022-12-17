even_number=0
odd_number=0
n= int(input("Enter a number "))
for i in range(1,n+1):
    if i%2==0:
        even_number = even_number+1
    else:
        odd_number = odd_number+1

print("Number of even numbers:",even_number)
print("Number of odd numbers:",odd_number)
