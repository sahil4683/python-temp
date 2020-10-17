# Sum of 1 to user enterd number
i=1
num=input("Enter a number")
num=int(num)
sum=0
while i<=num:
    sum=sum+i
    i=i+1
print(f"Sum is {sum}")