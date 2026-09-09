def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b==0:
        return "Not defined!"
    else:
        return a/b
while True:
    print("1.ADDITION")
    print("2.SUBTRACTION")
    print("3.MULTIPLICATION")
    print("4.DIVISION")
    print("5.Exit")
    choice=input("Enter your choice buddy(1/2/3/4/5):")
    if choice=="5":
        print("Thankyou for using....." )
        break

    number_1=float(input("Enter the first number:"))
    number_2=float(input("Enter the second number:"))

    if choice=='1':
        print("Answer is:",add(number_1,number_2))
    elif choice=='2':
        print("Answer is:",subtract(number_1,number_2))
    elif choice=='3':
        print("Answer is:",multiply(number_1,number_2))
    elif choice=='4':
        print("Answer is:",divide(number_1,number_2))
    else:
        print("INVALID CHOICE BUDDY")

    again=input("Continue?(yes/no): ")
    if again.lower()=="yes":
        continue
    else:
        break
 
