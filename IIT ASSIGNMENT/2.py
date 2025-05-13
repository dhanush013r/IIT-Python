"""Design a system to manage a fleet of drones. 
A class Device has basic device info. A class Flyer has the method fly()
 to simulate drone flying. A third class Drone inherits from both Device and Flyer, 
 and includes additional drone-specific actions like capture_image(). Create an object
   of Drone and demonstrate all functionalities ensuring no conflict arises between inherited methods.

"""
class d:
    def ini(self,n):
        self.n = n
    def s(self):
        print("device name =:",self.n)
class f:
    def f(self):
        print("drone flying")
class r(d,f):
    def c(self):
        print =("image captuered")

R=r("x")
R.s()
R.f()
R.c()

