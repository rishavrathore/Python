num = int(input("Enter a number upto which you want to print the series"))
num1,num2 = 0,1
print(num1,num2,sep=",",end=",")
for i in range(num):
    num3 = num1+num2
    num1,num2=num2,num3
    print(num3,end=",")

