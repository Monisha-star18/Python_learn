# Import our user-defined module
import add


# __name__ of this file
print("Inside main:")
print(__name__)


# We can still use functions from the imported module
result = add.addMethod(10, 30)

print("Result:", result)