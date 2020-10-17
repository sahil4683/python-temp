string="HTML is very good programming language python is markup laguage"

print(string.replace(" ","_"))
print(string.replace("is","was"))


p1=string.find("is")
p2=string.find("is",p1+1)
print(p1)
print(p2)