salary = int(input("what is your salary: "))
service = int(input("how many years of service: "))

if service > 10 :
    print(salary + 10%salary)
elif service > 6 :
        print(salary + 8%salary)

elif service < 6 :
            print(salary + 5%salary)

else: print("no bonus")