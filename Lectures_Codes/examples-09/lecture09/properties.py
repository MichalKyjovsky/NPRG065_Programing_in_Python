#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Sensor:
    def __init__(self):
        # Raw temperature stored as integer
        # Initialized to 20°C
        self._raw_temperature = 200

    # Get temperature in degrees
    @property
    def temperature(self):
        print('Getter called')
        return self._raw_temperature / 10

    # Set temperature using value in degrees
    @temperature.setter
    def temperature(self, value):
        print('Setter called')
        self._raw_temperature = int(value * 10)


class ReadonlySensor:
    def __init__(self, temp):
        self.__temp = temp

    @property
    def temperature(self):
        return self.__temp


class WriteonlySensor:
    def __init__(self, temp):
        self.__temp = temp

    def temperature(self, value):
        self.__temp = value

    temperature = property(fset=temperature)


sensor = Sensor()

# Read access
print(sensor.temperature)

# Write access
sensor.temperature = 23.554
print(sensor.temperature)

readonlySensor = ReadonlySensor(20)

print(readonlySensor.temperature)

# temperature is read only and cannot be changed
# Uncomment the following line to get an error
# readonlySensor.temperature = 10


writeonlySensor = WriteonlySensor(10)
writeonlySensor.temperature = 12

# temperature is write only and cannot be read
# Uncomment the following line to get an error
# print(writeonlySensor.temperature)