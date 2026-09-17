#inheritance - multiple level inheritance from  D-> c <-F
"""
Method Resolution Order (MRO) means:

MRO is the order in which Python searches the inheritance hierarchy for a method or attribute.

MRO is roughly: E → D → F → object

so first check in own class then the inheritance order 
"""
class D() :
    def func6 (self):
        print("func 6 works")

    #check 2 :if avaliable print 
    def show(self):
        print("show in D")

class F() :
    def func7 (self):
        print("func 7 works")

     #check 3 :if avaliable print 
    def show(self):
            print("show in F")

#as the inheritnace is D and then F it search in that way 
class E(D,F) :
    def func8 (self):
        print("func 8 works")

    #check 1 : if avaliable print 
    def show(self):
            print("show in E")


obj1 = E()

# obj1.show()

#dont change the inheritnace order but call the F show 
F.show(obj1)