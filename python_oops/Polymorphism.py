class Laptop:

    def build(self):
        print("Laptop builds")

class Desktop:

    def build(self):
        print("desktop builds")

#Alien doesn't actually care whether it receives a Laptop or Desktop.
#Duck typing means: Python cares about what an object can DO, rather than what class it belongs to.

class Alien:
    #The interesting part is that Alien doesn't inherit from Laptop. 
    #This is called composition / object collaboration.

    #also here machine:Laptop is a type hint means it hints it need a laptop object 

    def code(self, machine: Laptop):
        print("Alien Building..")
        machine.build()


asus_rog = Laptop()
hp = Desktop()

navin = Alien()

# navin.code(asus_rog)

#here the desktop object acts like the Laptop also , so just use it 
navin.code(hp)