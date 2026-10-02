class Car:
    def move(self):
        print("The car is driving.")


class Person:
    def move(self):
        print("The person is walking.")


class Robot:
    def move(self):
        print("The robot is moving.")


def make_it_move(obj):
    obj.move()


car = Car()
person = Person()
robot = Robot()

objects = [car, person, robot]

for obj in objects:
    make_it_move(obj)
