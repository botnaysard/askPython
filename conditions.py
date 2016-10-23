# LESSON

gender = input("Gender? ")

if gender.upper() == "MALE":
    print("Your cat is male.")
else:
    print("Your cat is female.")

age = int(input("Age? "))
if age < 5:
    print("Your cat is young.")
else:
    print("Your cat will probably die soon.")

# EXERCISES

# ask for a number between 1 and 10.  If the entry is outside that range, let the user know it's invalid
numero = int(input("Give me a number between 1 and 10. "))
if (numero >=1) and (numero <=10):
        print("Ya numba is: " + str(numero))
else:
    print("invalid entry!")

# ask for a password

userPass = "Monkey123"
userEntry = input("Password: ")
if userEntry == userPass:
    print("Login successful.")
else:
    print("Incorrect Password.")
