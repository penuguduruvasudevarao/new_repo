with open("name.txt","r") as file:
    print("using readlines():")
    lines=file.readlines()
for i in lines:
    print(i.strip())