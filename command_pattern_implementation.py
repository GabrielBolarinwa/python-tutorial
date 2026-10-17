from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class Light:
    @staticmethod
    def turn_on():
        print("Light is on")

    @staticmethod
    def turn_off():
        print("Light is off")

class LightOn(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_on()

class LightOff(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_off()

class Remote:
    def press(self, command):
        command.execute()

light = Light()
remote = Remote()

on = LightOn(light)
off=LightOff(light)

remote.press(on)
remote.press(off)