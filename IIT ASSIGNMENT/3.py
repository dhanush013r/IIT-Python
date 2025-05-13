"""Build a class hierarchy for an online learning platform.
 The base class User includes name and email. The subclass Instructor adds subject expertise 
 and a method to upload content. A third class CourseCreator (inherits from Instructor) allows creation 
 of complete courses with modules.
 Override the display_info() method at each level to reflect role-specific details."""
class u:
    def ini(self,n,e):
        self.n =n
        self.e=e 
        def i(self):
            print(f"u: {self.n} , e: {self.e}")
class i(u):
     def ini(self,n,e):
         super().ini(n,e)
         self.s=s
     def u(self):
         print(f"{self.n} uploaded for {self.s}")
     def i (self):
         print(f"i:{self.n}, e:{self.e} ,S:{self.s}")
class c(i):
    def ini(self,n,e):
        super().ini(n,e,s)
        self.m =m
    def c(self):
        print(f"c with:{','.join(self.m)}")
    def i(self):
        print (f"cc:{self. n},e:{self.e},s:{self.s},m:{','.join(self.m)}")
               