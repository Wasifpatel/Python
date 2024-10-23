#if else statements
a=4
b=5

if(a>b):
    print("a is greater")
else:
    print("b is greater")
    

light ='yellow'

if(light=="red"):
    print("stop")
elif(light=="green"):
    print("go")
elif(light=="yellow"):
    print("look")
else:
    print("light is broken")


age =20

if(age >=18):
    print("can vote")# 4 gaps after if statement is called indentation
else:
    print("can't vote")


marks=int(input("Enter students marks: "))
if(marks>=90):
    print("Grade A")
elif(marks>=80 and marks<=90):
    print("Grade B")
elif(marks>=70 and marks<=80):
    print("Grade C")
elif(marks>70):
    print("Grade D")
else:
    print("Fail")


#nested if 
age=34

if(age>=18):
   if(age>=80):
      print("cannot drive")
   else:
       print("can drive")
else:
    print("cannot drive")



    
