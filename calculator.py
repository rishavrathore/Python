def add(num1,num2):
    result=num1+num2
    return result
def sub(num1,num2):
    result=num1-num2
    return result
def product(num1,num2):
    result=num1*num2
    return result
def divide(num1,num2):
    result=(num1/num2)
    return result

print("select operation.")
print("1.add")
print("2.sub")
print("3.product")
print("4.divide") 

while True:
    choice = input("Enter choice(1/2/3/4): ")

    if choice in ('1','2','3','4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1,"+",num2,"=",add(num1,num2))
        elif choice =='2':
            print(num1,"-",num2,"=",sub(num1,num2))   
        elif choice == '3':
            print(num1,"*",num2,"=",product(num1,num2))
        elif choice == '4':
            print(num1,"/",num2,"=",divide(num1,num2))  


        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            break
    else:
        print("Invalid Input")               