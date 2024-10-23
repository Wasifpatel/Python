str1="This is string"
str2='Apna College'
str3=str1 + " " +str2

print(str3)
print(len(str2))
print(str1[0])


#Slicing in strings
str2='Apna College'
print(str2[1:6])
print(str2[5:12])
print(str2[:4])#[0:4]
print(str2[5:])#[5:len(str2)]

# Negative index
str="Apple"
print(str[-3:-1])

#String Functions
str = "i am a coder."
print(str.endswith("er."))  #returns true if string ends with substr 
print(str.capitalize())  #capitalizes 1st char 
print(str.replace("am","am new"))#replaces all occurrences of old with new 
print(str.find("code"))  #returns 1st index of 1st occurrence 
print(str.count("a")) #counts the occurrence of substr in string
print(str.split())

name=input("enter your name: ")
print("my name is ",name)
print("length is ",len(name))
