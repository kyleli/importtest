class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property # A property removes the need for ()
    def WhoAmI(self):
        print(f"I am {self.name} age {self.age}.")
    
p1 = Person("John", 20)
p1.WhoAmI