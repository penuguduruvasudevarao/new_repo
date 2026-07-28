name=input("name: ")
age=int(input("age: "))
college=input(("college: "))
with open("student.txt","a") as file:
    file.write("name "+name + "\n")
    file.write("age"+str(age) + "\n")
    file.write("college"+college + "\n")