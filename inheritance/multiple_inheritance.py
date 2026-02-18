class Person:
    def __init__(self, name):
        self.name = name
        print("Person constructor called")

    def greet(self):
        print("Hello, my name is", self.name)


class Athlete:
    def __init__(self, sport):
        self.sport = sport
        print("Athlete constructor called")

    def play(self):
        print("I play", self.sport)


# Multiple inheritance
class StudentAthlete(Person, Athlete):
    def __init__(self, name, sport, grade):
        Person.__init__(self, name)      # Initialize first parent
        Athlete.__init__(self, sport)    # Initialize second parent
        self.grade = grade
        print("StudentAthlete constructor called")

    def introduce(self):
        print(f"I am {self.name}, I play {self.sport}, and I'm in grade {self.grade}.")


# Create object
x = StudentAthlete("Mike", "Basketball", 12)

x.greet()
x.play()
x.introduce()