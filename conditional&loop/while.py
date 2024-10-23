n=int(input("enter number:"))

while n <= 10:
    if(n % 2 != 0 ):
        print(n)
    n+=1

age =28
if(age>=18 and age<=28):
    print("you are teenager")
elif(age>=28 and age <=50):
    print("you are middle age ")
else:
    print("you are older")