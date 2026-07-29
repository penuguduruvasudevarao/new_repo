class Student:
    def __init__(self):
        self.__password="abc123"
    def get_password(self):
        return self.__password
s=Student()
print(s.get_password())


print("It's a getter method")