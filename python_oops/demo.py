
class computer:

    def __init__(self,cpu,ram,ssd):
        print("init called")
        self.CPU = cpu
        self.RAM = ram
        self.SSD = ssd

    def config(self): #self act like this in js 
        print(f"The configuartion ram : {self.RAM} , cpu : {self.CPU} , ssd : {self.SSD} , {self}")

com1 = computer("i3","8GB","512GB")
com2 =computer("i7","16GB","1TB")


com1.config()
com2.config()

# computer.config(com1)
# computer.config(com2)
