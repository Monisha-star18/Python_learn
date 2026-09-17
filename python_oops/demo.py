
class computer:

    #it is a class  variable , it is for all object the same 
    brand = "HP"

    #it is a instance method - > method work with the object 
    def __init__(self,cpu,ram,ssd):
        print("init called")
        #it is a instance variable
        self.CPU = cpu
        self.RAM = ram
        self.SSD = ssd
  
    #it is a instance method
    def config(self): #self act like this in js 
        print(f"The configuartion ram : {self.RAM} , cpu : {self.CPU} , ssd : {self.SSD} , {self}")

    #its a class method 
    # we use a class method when we need to access a class variable 
    #and we use a instance method to access an instance variable 
    @classmethod
    def brandInfo(cls):
        return cls.brand

    #it is a static method , not based on any class variable or instance variable 
    #it is a utility method 
    @staticmethod
    def gb_to_byte(gb):
        return gb * (1024 ** 3 )

com1 = computer("i3","8GB","512GB")
com2 =computer("i7","16GB","1TB")


com1.config()
com2.config()

# computer.config(com1)
# computer.config(com2)

print(computer.brandInfo())

print(computer.gb_to_byte(16))
