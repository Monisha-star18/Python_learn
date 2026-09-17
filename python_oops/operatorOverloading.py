"""
Operator overloading syntax 

class Something:

    def __operator_method__(self, other):
        # define what the operator should do

Methods are:

__add__()       [+]    __sub__()       [-]
__mul__()       [*]    __truediv__()   [/]
__floordiv__()  [//]   __mod__()       [%]
__pow__()       [**]

__eq__()        [==]     __ne__()        [!=]
__gt__()        [>]      __lt__()        [<]
__ge__()        [>=]     __le__()        [<=]

__and__()       [&]      __or__()        [|]    __xor__()       [^]
"""


class Students:

    def __init__(self,marks):
        self.marks = marks

    # here without this operator overloading the == of the object work and tell whether the object are equal or not
    #but as we mentioned to check the marks it works accordingly 
    def __eq__(self,other):
        return self.marks == other.marks

stu1 = Students(80)
stu2 =Students(90)
stu3 = Students(80)

## without the __eq__ func it return false and false as the objects are not same , ad we implemented object overloading and 
## make it to check on the mark so it is working on marks and giveing answer and not on the object alone 
print(stu1 == stu2)
print(stu1 == stu3)
        