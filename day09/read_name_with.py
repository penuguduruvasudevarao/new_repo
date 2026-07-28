with open("name.txt","r") as file:
    lines=file.readlines()
    print("content of the file :" ,lines)
for i in lines:
    print(i.strip())