#!/usr/bin/python3

class Laptop:
    pass

class Decimal:
    pass

class Seventh_Grade_Student:
    #every object of type Peson will have both of these atributes
    age  = 12

    def __init__(self, name: str='', gpa: float=''):
        self.name = name
        self.gpa = gpa

    def say_hello(self):
        return f"Helllo, I am {self.name}"

Kevin = Seventh_Grade_Student('Kevin', 2.90)
Johnson = Seventh_Grade_Student('Johnson', 2.70)

print(Kevin)
print(Kevin.name) #this prints Kevin
print('Kevins age:', Kevin.age)
print('Seventh grade student age:', Seventh_Grade_Student.age)
print(Kevin.gpa)
print(Kevin.say_hello)

print(Johnson)
print(Johnson.name) #this prints Johnson
print(Johnson.gpa)
print(Johnson.age)
print(Seventh_Grade_Student.say_hello)
