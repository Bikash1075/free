# problem 1
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
    
# 2nd approach
import json
class Employee:
    def __init__(self):
        self.Employeesdata={}
        self.e1={"emp1":{"Name" : "Bikash Ranjan Padhy" , "DOB" : "29/10/1994", "Hieght" : "5'8" , "City" : "Surada" , "State" : "Odisha" }}
        self.e2={"emp2":{"Name" : "Firoz Ansari" , "DOB" : "22/05/1996", "Hieght" : "5'4" , "City" : "Jamshedpur" , "State" : "Jharkhand" }}
        self.e3={"emp3":{"Name" : "Srinu Ponduru" , "DOB" : "15/07/1996", "Hieght" : "5'10" , "City" : "Beemavaram" , "State" : "Andhra Pradesh" }}
        self.e4={"emp4":{"Name" : "Abhishek Priyadarshi" , "DOB" : "25/03/1997", "Hieght" : "5'8" , "City" : "Patna" , "State" : "Bihar" }}
        self.e5={"emp5":{"Name" : "Jeetendra Kumar" , "DOB" : "25/08/1991", "Hieght" : "5'5" , "City" : "Budhana" , "State" : "Uttar Pradesh" }}
        self.e6={"emp6":{"Name" : "Shivangee Mishra" , "DOB" : "10/08/1996", "Hieght" : "5'5" , "City" : "Jodhpur" , "State" : "Rajasthan" }}
        self.e7={"emp7":{"Name" : "Kiran Pattnaik" , "DOB" : "15/9/1995", "Hieght" : "5'8" , "City" : "Pune" , "State" : "Maharastra" }}
        self.e8={"emp8":{"Name" : "Abhishek Panda" , "DOB" : "22/8/1995", "Hieght" : "5'9" , "City" : "Jaipur" , "State" : "Odisha" }}
        self.emp_list=[self.e1,self.e2,self.e3,self.e4,self.e5,self.e6,self.e7,self.e8]
        for i in self.emp_list:
            self.Employeesdata.update(i)
        with open ("employee.json","w") as e:
            self.x=json.dump(self.Employeesdata,e)
    def read_Emp_data(self):
        with open("employee.json","r") as e_read:
            self.Employee=json.load(e_read)
        for i, j in self.Employee.items():
                print (i,"=",j)    
e= Employee()
e.read_Emp_data()

# problem 2
import json
state_capital={"Odisha":"Bhubaneswar", "West Bengal":"Kolkata", 
"Punjab":"Chandigarh", "Bihar":"Patna", 
"Uttar Pradesh":"Kanpur", "Karnataka":"Bengaluru", "Maharastra":"Mumbai"}

with open("State_Capital.json","w") as S_C:
    json.dump(state_capital,S_C)