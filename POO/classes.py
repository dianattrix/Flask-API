class Person():
    def __init__(self, name):
        self.name = name
    def sayHi(self):
        self.text = "Hi! My name is " + self.name
        return self.text

person1 = Person("Diana")
print(type(person1))

print(person1.name)
print(person1.sayHi())

# heritance

class Adult(Person):
    def __init__(self, name):
        Person.__init__(self, name)
    # overwriting functions
    def sayHi(self):
        self.text = "I am an adult"
        return self.text
    # str function
    def __str__(self):
        self.text = "Adult, name: " + self.name
        return self.text

adult1 = Adult("Diana")
print(type(adult1))

print(adult1.sayHi())
print(adult1)
