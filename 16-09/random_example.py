import random

low =1 
high = 100

# number = random.randint(1, 10)

# number = random.randint(low,high)

# number = random.random()
# print(number)


options = ["rock","paper","scissors"]

optionPicked = random.choice(options)

print(optionPicked)

print(options)
#the shuffle dont support tuple object 
random.shuffle(options)
print(options)