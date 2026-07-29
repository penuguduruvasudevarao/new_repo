class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary 

    def display(self):
        print(self.name)
        print(self.salary) 

name=input("Enter your name :")
salary=int(input("Enter your salary :"))
e1=Employee(name,salary)
e1.display()