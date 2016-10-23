# LESSON
name = input('What is your name? ')
print('Howdy, ' + name)

job = input('Whatcha do? ')
print('You ' + job + '?!?')

num = input('Give me a number, please. ')
print ('You said: ' + str(num))

# EXERCISES

print("\n")

# make a program that asks a phone number

telefono = input("what's your number, baby? (without dashes, please.)")
convertText = str(telefono)
print("I'll call you at " + telefono[0:3] + '-' + telefono[3:6] + '-' + telefono[6:10] + " later.")

# make a program that asks for the user's preferred programming language

lingo = input("What's yer fave language to code in? ")
if lingo.upper() == "PYTHON":
    print("You're a cool dude!  Python is the BEST!!!")
else:
    print("What is that?")

# Q: What's the difference between input in Python 2 & 3?
# A: Python2 uses "raw_input()" whereas Python3 uses "input()