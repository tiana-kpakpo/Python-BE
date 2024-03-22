#user information 
#name, age, DoB

user = {
    "name": "james Doe",
    "age": 32,
    "DOB": "1995-31-12"
}

# classes 

class User: 
    #constructor (methods// fxns)
    def __init__(self, name: str, age: int) -> None: 
        self.name = name
        self.age = age

    def greet(self) -> None:
        print(f"Welcome to the app {self.name}")

    def can_vote(self) -> bool:
        return self.age >= 18    


# instantiating a class      
user = User("James Doe", 43)
user.greet() 
print(user.name) 
user.name = "John Doe"   
user.greet() 
print(user.can_vote())


### to make a variable private in python we use the _/__ to make it and unchangeable by user (_name)



# data classes

from dataclasses import dataclass
# import datetime
# import dataclasses


# @dataclasses.dataclass  ## decorator 
@dataclass
class Student:
    name: str
    level: int
    gender: str
    programme: str

def greet(cls) -> None:
    print(f"Welcome to the app {cls.name}")    


student = Student("Jame Doe", 200, "Male", "Engineering" )
print(student.programme)
student.programme = "IT"
print(student.programme)
# student.greet()

