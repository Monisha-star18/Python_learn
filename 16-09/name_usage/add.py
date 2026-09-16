# This is a user-defined module

def addMethod(a, b):
    return a + b


# Print the value of __name__ inside this file
print("Inside userDefinedModules:")
print(__name__)

def main():
    print(addMethod(10,20))


# This will run ONLY when this file is executed directly
if __name__ == "__main__":
    main()
    print("userDefinedModules.py is running directly")