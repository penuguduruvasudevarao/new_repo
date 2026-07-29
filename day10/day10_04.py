try:
    with open("students.txt","r") as file:
       print(file.read())
except FileNotFoundError:
    print("The File doesn't exist")