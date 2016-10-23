# LESSON

# create and open file

f = open("test.txt", "a")

# write data to file

f.write("Don't delete existing data \n")
f.write("Add this to the existing file.")

# close file
f.close()

# EXERCISE

people = ["Dave", "Jimmy", "Steve", "Antonio"]
nameFile = open("people.txt", "a")

for i in people:
    nameFile.write(i + "\n")

nameFile.close()