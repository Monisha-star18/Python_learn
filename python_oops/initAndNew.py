"""
__new__ creates the object.
__init__ initializes the object.

also to tell new is a constructor and init is a initializer 

init is not a constructor , it is just a initializer that initializes the instance variable
"""


class Car :

    def __new__(cls,name):
        print("new method called")
        #call the init 
        return super().__new__(cls)

    #it is a instance method - > method work with the object 
    def __init__(self,name):
        print("init called")
        self.Name = name 

    #it is a instance method
    def display(self):
        print(f"Hello {self.Name} welcome to the site")



#normal object creation 
ob1 = Car("Monisha")

ob1.display()

#object creation using __new__
ob2 = Car.__new__(Car,"Sam")

Car.__init__(ob2, "Sam")

ob2.display()