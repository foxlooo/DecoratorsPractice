from log import log_decorator

class Temperature:

    def __init__(self, celsius=0):
        self._celsius = celsius

    @property
    @log_decorator("temperature.log")
    def celsius(self):
        return self._celsius

    @celsius.setter
    @log_decorator("temperature.log")
    def celsius(self, celsius):
        if celsius > -273:
            self._celsius = celsius
        else:
            raise Exception("You cannot have a temperature under -273 Celsius (Absolute Zero)")

    @celsius.deleter
    @log_decorator("temperature.log")
    def celsius(self):
        self._celsius = 0

    @property
    @log_decorator("temperature.log")
    def fahrenheit(self):
        return self._celsius*9/5 + 32

    @fahrenheit.setter
    @log_decorator("temperature.log")
    def fahrenheit(self, fahrenheit):
        if fahrenheit > -459:
            self._celsius = (fahrenheit - 32)*5/9
        else:
            raise Exception("You cannot have a temperature under -459 Fahrenheit (Absolute Zero)")

    @fahrenheit.deleter
    @log_decorator("temperature.log")
    def fahrenheit(self):
        self._celsius = 0

temp1 = Temperature()

temp1.celsius = 100
print(temp1.celsius)
temp1.fahrenheit = 100
print(temp1.fahrenheit)
print(temp1.celsius)
temp1.celsius = -300