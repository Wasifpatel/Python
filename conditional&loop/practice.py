num=int(input("enter the number: "))

if(num % 2 == 0):
    print("number is even")
else:
    print("number is odd")

#greatest between three numbers

num1=int(input("enter the number 1: "))
num2=int(input("enter the number 2: "))
num3=int(input("enter the number 3: "))

if((num1 > num2) and (num1>num3)):
    print(num1," is greater")
elif((num2 > num3) and (num2>num1)):
    print(num2," is greater")
else:
    print(num3," is greater")