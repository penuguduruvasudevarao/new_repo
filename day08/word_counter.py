sentence=input("enter a sentence")
list_a=sentence.split(" ")
set_a=set(list_a)
for i in set_a:
    print(i," : ",list_a.count(i))