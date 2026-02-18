class Person:
    def greet(self):
        print("Hello! I am a person.")


class Student(Person):
    # Overriding the greet() method
    def greet(self):
        print("Hello! I am a student.")


# Create objects
p = Person()
s = Student()

p.greet()  # Calls Person's method
s.greet()  # Calls Student's overridden method