class A:
    def func_1(self):
        print("This function is defined inside the parent class.")

class B(A):
    def func_2(self):
        print("This function is defined inside the child class.")

my_object = B()

my_object.func_1()
my_object.func_2()
