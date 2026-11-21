
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature cannot be below -273.15 Celsius!")
        self._celsius = value

    @property
    def kelvin(self):
        return self._celsius + 273.15


t1 = Temperature(25)

print("Celsius:", t1.celsius)
print("Kelvin:", t1.kelvin)

t1.celsius = 30

print("Updated Celsius:", t1.celsius)
print("Updated Kelvin:", t1.kelvin)
