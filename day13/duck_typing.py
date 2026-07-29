class Student:
    def show(self):
        print("Student")
class Teacher:
    def show(self):
        print("Teacher")



def display(person):
    person.show()
display(Student())
display(Teacher())
