# LESSON & EXERCISES

class Website:
    def __init__(self, title, location):
        self.title = title
        self.location = location

    def showTitle(self):
        print(self.title)

    def showLoc(self):
        print(self.location)

obj = Website('askpython.com', 'Stockholm')
obj2 = Website('scotthayward.io', 'Ottawa')
obj.showTitle()
obj2. showTitle()
print("\n")
obj.showLoc()
obj2.showLoc()