string = input("Enter a String ")
reverse_string = ''
for i in string:
    reverse_string= i+reverse_string
    print(reverse_string)
print(reverse_string)

s= input("enter a string ")
rev="".join(reversed(s))
print(rev)



string= input("Enter a String ")
rev=string[-1::-1]
print(rev)


string= input("Enter a String ")
rev= lambda x:x[::-1]
print(rev(string))

s='chris alan'
s=s.title()
print(s)


