
class Bird:
    def fly(self):
        print("Bird flies using wings")


class Airplane:
    def fly(self):
        print("Airplane flies using engines")


class Drone:
    def fly(self):
        print("Drone flies using propellers")


def make_it_fly(obj):
    obj.fly()


bird = Bird()
airplane = Airplane()
drone = Drone()

make_it_fly(bird)
make_it_fly(airplane)
make_it_fly(drone)
