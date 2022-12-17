import json
employees={}
e1={"emp1":{"Name" : "Bikash Ranjan Padhy" , "DOB" : "29/10/1994", "Hieght" : "5'8" , "City" : "Surada" , "State" : "Odisha" }}
e2={"emp2":{"Name" : "Firoz Ansari" , "DOB" : "22/05/1996", "Hieght" : "5'4" , "City" : "Jamshedpur" , "State" : "Jharkhand" }}
e3={"emp3":{"Name" : "Srinu Ponduru" , "DOB" : "15/07/1996", "Hieght" : "5'10" , "City" : "Beemavaram" , "State" : "Andhra Pradesh" }}
e4={"emp4":{"Name" : "Abhishek Priyadarshi" , "DOB" : "25/03/1997", "Hieght" : "5'8" , "City" : "Patna" , "State" : "Bihar" }}
e5={"emp5":{"Name" : "Jeetendra Kumar" , "DOB" : "25/08/1991", "Hieght" : "5'5" , "City" : "Budhana" , "State" : "Uttar Pradesh" }}
e6={"emp6":{"Name" : "Shivangee Mishra" , "DOB" : "10/08/1996", "Hieght" : "5'5" , "City" : "Jodhpur" , "State" : "Rajasthan" }}
e7={"emp7":{"Name" : "Kiran Pattnaik" , "DOB" : "15/9/1995", "Hieght" : "5'8" , "City" : "Pune" , "State" : "Maharastra" }}
e8={"emp8":{"Name" : "Abhishek Panda" , "DOB" : "22/8/1995", "Hieght" : "5'9" , "City" : "Jaipur" , "State" : "Odisha" }}
emp_list=[e1,e2,e3,e4,e5,e6,e7,e8]
for i in emp_list:
    employees.update(i)
with open ("employee.json","w") as e:
    json.dump(employees,e)

with open("employee.json","r") as e_read:
    Employee=json.load(e_read)
for i, j in Employee.items():
    print (i,"=",j)