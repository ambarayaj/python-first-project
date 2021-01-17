class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

john = Person('John', 22)
Mariam = Person('Mariam', 18)

print(john.name + ' ' + str(john.age))
print(Mariam.name + ' ' + str(Mariam.age))