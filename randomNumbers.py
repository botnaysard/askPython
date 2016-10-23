#LESSON
import random

print("LESSON")
# create random float
print(random.random())

# create random integer between 1 and 10
print(random.randrange(0,10))

#create random float between 1 and 10

print(random.uniform(1,10))



# EXERCISES
print("\n")
print("EXERCISES")

# create a random number and store it in variable x
x = random.randrange(1, 100)
print(x)
print("\n")

# print three random numbers
for counter in range (1, 4):
    print("float" + str(counter) +": " +str(random.random()))