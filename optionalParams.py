# LESSON
# NOTE: to make a parameter option, append "=None" to the parameter

def addNumbers (a,b,c=None):
    if c is not None:
        return a+b+c
    else:
        return a+b

print(addNumbers(1,2))
print(addNumbers(1,2,3))

# EXERCISES
# create a function that can be called like this:
# person("abraham")
# person("abraham","lincoln")

def person (f, l=None):
    if l is not None:
        print(f + " " + l + " is a cool dude.")
    else:
        print(f + " is a cool dude.")

person("Dave")
person("Willy","Chilly")
