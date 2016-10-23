# LESSON

x = 3
while x < 10:
    print(x)
    x += 1

# EXERCISES

print("\n")

# make a program that multiplies itself by 2 until it is larger than 128

y = 1
while y <= 128:
    print(y)
    y = y * 2

# Ask a number until it is correct

import random
target = random.randrange(1,10)
guess = int(input("guess a number between 1 and 10: "))
while guess != target:
    if guess >= 1 and guess <=10:
        if guess != target:
            guess = int(input("try again: "))
        if guess == target:
            print("Good guess!")
    else:
        guess = int(input("Invalid input, try again: "))
