# print(help("modules"))

# use the import keyword to use a module
#normal
import math 

# import with aliase
import math as m 

# only the function 
from math import pi 

#import the user defined function 
import userDefinedModules as udm

#to use it mention the module and function like module.function()
print(m.pi)
print(pi)

#function in user defined modules
print(udm.pi)

square = udm.square(2)
cube = udm.cube(5)

print(f"square of 2 : {square} , cube of 5 :{cube}")

print(f"circumference : {udm.circumference(3)} , area : {udm.area(5)}")

