x=lambda a : a + 10
print("Addition is",x(3))
print("\n")

x=lambda a,b:a*b
print("Multiplication is",x(3,5))

print("\n")
x = lambda a, b, c : a + b + c
print(x(15, 6, 2))

print("\n")
def myfun(n):
    return lambda a:a * n

doubler=myfun(2)
tripler=myfun(3)

print("Doubled value ",doubler(10))
print("Trippled value",tripler(20))