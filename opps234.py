from abc import ABC, abstractmethod

class smartdevices(ABC):

    def show_device(self,name):
        print("Device name:",name)

    @abstractmethod
    def turn_on(self):
        pass

class smartlight(smartdevices):
    def turn_on(self):
        print("Smart light is turned on")

class smartfan(smartdevices):
    def turn_on(self):
        print("Smart fan turned on")

class smartspeaker(smartdevices):
    def turn_on(self):
        print("Smart speaker is turned on")

light = smartlight()

fan = smartfan()
speaker = smartspeaker()

light.turn_on()
light.show_device("LIGHT")
fan.turn_on()
fan.show_device("FAN")
speaker.turn_on()
speaker.show_device("SPEAKER")


class security_camera:
    def check_status(self):
        print("RECORDING")

class door_lock:
    def check_status(self):
        print("Secure")

devices = [security_camera(), door_lock()]
print("SMART DEVICES STATUS")
for device in devices:
    device.check_status()