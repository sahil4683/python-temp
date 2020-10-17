# Print count of each word

name=input("Enter your name ")
temp_var=""
i=0
for i in range(len(name)):
    if name[i] not in temp_var:
        temp_var +=name[i]
        print(f"{name[i]} : {name.count(name[i])}")
    i +=1