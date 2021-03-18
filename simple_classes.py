
d = list()   # list d = new list();
d = []       # same
d.append(5)
d.append("wombat")
print(d)

class Animal:
    def get_habitat(self):
        return "swamp"

class ErrorFile:
    pass

class Dog(Animal):
    def bark(self):
        print("woof woof")

d = Dog()
d.bark()   # Dog.bark(d)
print(d.get_habitat())
d2 = Dog()
d2.bark()  # Dog.bark(d2)

