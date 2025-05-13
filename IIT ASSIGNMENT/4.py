"""Problem Statement: You are developing a system to control smart appliances.
 Create a base class Appliance with a method status() that prints a default message.
   Subclasses like Fan, Light, and AC override this method to give device-specific status updates. 
   Store all devices in a list and iterate through it, invoking the status() method to demonstrate polymorphism."""
class ap:
    def s(self):
        print("general appliance status.")
class f(ap):
     def s(self):
        print("fan is on")
class l(ap):
     def s(self):
        print("light is on")
class a(ap):
     def s(self):
        print("ac is cooling")
d=[f(),l(),a()]
for device in d:
    device.s()
