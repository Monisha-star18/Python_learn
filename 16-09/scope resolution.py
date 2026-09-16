#varibale scope - >where a varibale is visible and accessible 

#scope resolution (LEGB) ->  Local , Enclosed , Global , Built - in 


#Local scope 

def func1():
    #local to this function and can only used here 
    a=1
    print(a)

def func2():
    #local to this function and can only used here 
    b=2
    print(b)
    #try to print(a) it will give error as it local at func1 


"""
when it comes to enclosed , first it looks for any local variable 
else use the enclosed one 

"""
def func3 ():
    #enclosed scope 
    x = 1 
    def func4 ():

        #x=2  #local scope 
        print(x)
    func4()


func1()
func2()
func3()

#gobal 

""" exmaple 1 """

# y =3 

# def func5 ():
#     print(f"value of y inside function : {y}")


# func5()
# print(f"value of y outside function : {y}")


""" exmaple 2 """

# y =3 

# def func5 ():
#       y = 2 
#     print(f"value of y inside function : {y}")


# func5()
# print(f"value of y outside function : {y}")

""" exmaple 3 
If you use the global keyword, the variable belongs to the global scope:
"""


# def func5 ():
#     global y  # y is local but we used the global keyword and make it  a global varibale 
#     y=2
#     print(f"value of y inside function : {y}")


# func5()
# print(f"value of y outside function : {y}")

""" exmaple 4 """

y=3 

def func5 ():
    global y  # y is local but we used the global keyword and make it  a global varibale 
    y=2
    print(f"value of y inside function : {y}")


func5()
print(f"value of y outside function : {y}")


"""
built -in 

This example demonstrates Python's scope resolution (LEGB). 
The e imported from math is initially available, but then e = 3 creates a global variable named e.
When func1() runs, Python first looks for e inside the function (Local scope), 
then checks Enclosed, Global, and Built-in scopes. Since there is no local e, 
it finds the global e = 3, so the function prints 3.
"""
from math import e

e = 3

def func6():

    print(e)

func6()

