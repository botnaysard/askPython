# LESSON

city = ['Tokyo', 'NYC', 'Toronto', 'Philadelphia', 'Ottawa', 'London', 'Shanghai']
print("List of cities:\n")
for x in city:
    print("City" +  x)

print("\n")

num = [1,2,3,4,5,6,7,8,9,10]
print("Multiplications:")
for x in num:
    y =  x * (x - 1)
    print(str(x) + " x " + str(x - 1) + " = " +str(y))

# EXERCISES

print("\n")

# create a loop that prints every city in the provided list

cities = ['Barcelona','Madrid','Bilbao','Paris']
for x in cities:
    print(x)

# create a loop that prints the numbers from 1 to 10

print("\n")

count = 1
for i in range(10):
    print(count)
    count += 1
