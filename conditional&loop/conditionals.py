print("Welcome to rollcoaster")
height=int(input("Enter your height:"))

if height>120:
    print("You can ride")
else:
    print("You cannot ride")



number=int(input("Enter number:"))
if(number % 2==0):
    print("Number is even")
else:
    print("Number is odd")


height1=int(input("Enter your height:"))
age=int(input("Enter your age:"))

if height1>120:
    if age > 18:
        print("Pay 12 Rs")
    else:
        print("Pay 7 Rs")
else:
    print("you cannot ride")