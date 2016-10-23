# LESSON

def f(x,y):
    return x*y

print(f(3,4))

print("\n")

def sumA(list):
    sumA = 0
    for l in list:
        sumA = sumA + l
    return sumA

mylist = [1,2,3,4,5]
print(sumA(mylist))

# EXERCISES

#make a function that adds two numbers

def addStuff(a,b):
    c = a + b
    return c

userA = int(input("enter and integer: "))
userB = int(input("enter another: "))
print(addStuff(userA,userB))

print("\n")

def printNAme(userName):
    print("Your name is: " + userName)

enteredName = "Scott Hayward"
printNAme(enteredName)