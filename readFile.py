# LESSON
# read file line by line

filename = "readFile.py"

with open(filename) as f:
    content = f.readlines()

print(content)

infile = open(filename, 'r')
data = infile.read()
infile.close()

print(data)

textfile = "readFile.txt"

infile2 = open(textfile, 'r')
data2 = infile2.read()
infile2.close()

print(data2)