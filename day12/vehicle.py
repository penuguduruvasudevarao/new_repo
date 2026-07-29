class Vehicle:
    def start(self):
        print("vehicle is started")
    def stop(self):
        print("Vehicle is stopped")


class Car(Vehicle):
    def drive(self):
        print("Car is driving")
car1=Car()
car1.start()
car1.drive()
car1.stop()
