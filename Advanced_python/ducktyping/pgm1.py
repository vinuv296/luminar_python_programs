class Swift:
    def start(self):
        print("swift car start method")
    def accelerate(self):
        print("swift car can accelearte")
    def brk(self):
        print("swift car can break")

class Innova:
    def start(self):
        print("innova car start method")
    def accelerate(self):
        print("innova car can accelearte")
    def brk(self):
        print("innova car can break")

class Person:
    def drive(self,car):
        car.start()
        car.accelerate()
        car.brk()
sw=Swift()
ino=Innova()
p=Person()
p.drive(sw)
