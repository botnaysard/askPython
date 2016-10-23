# text

x = "I'm Nancy."
print(x)

# numbers and text
# NOTE: modified exercise to see if I could use a variable as an input prompt.  I can.
s = "My luck numero is %d, what is yours? " % 7
t = input(s)
print("Cool, so your lucky number is " + str(t) + ".")

# alternate method of combining strings and numbers
# NOTE: inadvertently completed this exercise above, and in previous exercises

# print character by index
print(x[0])
# NOTE: as with other languages, python appears to treat strings as an array of characters.  The first entry in the array is [0]

# print a piece of a string

print(x[0:3])