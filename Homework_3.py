import random

class Student:
    def __init__(self, name):
        self.name = name
        self.money = 1000
        self.knowledge = 50
        self.energy = 100
        self.happiness = 50
        self.day = 0

    def study(self):
        print("Student is studing")
        self.knowledge += 10
        self.energy -= 15
        self.happiness -= 5

    def work(self):
        print("Student is working")
        earned = random.randint(100, 300)
        self.money += earned
        self.energy -= 20
        self.happiness -= 10
        print(f"earned: {earned}")

    def rest(self):
        print("Student is chilling")
        self.energy += 20
        self.money -= 50
        self.happiness += 10

    def play(self):
        print("Student is playing")
        self.happiness += 15
        self.energy -= 10
        self.money -= 100

    def is_alive(self):
        if self.energy <= 0:
            print("The student is too tired")
            return False
        if self.knowledge <= 0:
            print("The student was expelled")
            return False
        if self.money <= -500:
            print("The student went bankrupt")
            return False
        return True

    def next_day(self):
        self.day += 1
        print(f"Day {self.day}")
        print(f"Money: {self.money} Knowledge: {self.knowledge} Energy: {self.energy} Happiness: {self.happiness}")


        if self.money < 200:
            self.work()
        elif self.knowledge < 40:
            self.study()
        else:
            action = random.choice([self.study, self.work, self.rest, self.play])
            action()


        self.energy -= 5
        self.happiness -= 2



student = Student("Arsen")

for _ in range(365):
    if not student.is_alive():
        break
    student.next_day()

print("Simulation is over!")