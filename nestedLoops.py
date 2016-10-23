# LESSON

persons = ["John", "Marissa", "Pete", "Dayton"]
restaurants = ["Mucho Burrito", "McDonald's", "Dominos", "Poop Station"]

for p in persons:
    for r in restaurants:
        print(p + " eats at " + r)

# EXERCISES

# print every tic tac toe position

vert = ["a", "b", "c"]
hori = ["1", "2", "3"]

for v in vert:
    for h in hori:
        print("position: " + v + h)

# make each person meet each other person in "persons"

for person1 in persons:
    for person2 in persons:
        if person1 is not person2:
            print(person1 + " please meet " + person2)