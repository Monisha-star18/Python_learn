"""
class A :
    def func1 (self):
        print("func 1 works")

    def func2 (self):
        print("func 2 works")

#inheritance - singe level inheritance from A->B
class B(A) :
    def func3 (self):
        print("func 3 works")

    def func4 (self):
        print("func 4 works")

#inheritance - multi level inheritance from A->B->C
class C(B) :
    def func5 (self):
        print("func 5 works")


#inheritance - multiple level inheritance from  D-> c <-F
class D() :
    def func6 (self):
        print("func 6 works")
class F() :
    def func7 (self):
        print("func 7 works")

class E(D,F) :
    def func8 (self):
        print("func 8 works")



obj1 = A()
obj1.func1()

obj2= B()
obj2.func2()

obj3 = C()
obj3.func1()
obj3.func3()

obj4 = E()
obj4.func6()
obj4.func7()

"""

#init and super method with inheritance

# all class in python are chile class  
#by default they inherit a object class 

class A :
    def __init__(self):
        print("init in A ")
        
    def func1(self):
        print("func1 works")

class B(A) :
    def __init__(self):
        #to call the parent class __init__ user super()
        super().__init__()
        print("init in B ")
        
    def func2(self):
        # to call a function from the parent class either use super or self 
        super().func1() 
        self.func1()
        print("func2 works")

obj1 = B()
obj1.func2()