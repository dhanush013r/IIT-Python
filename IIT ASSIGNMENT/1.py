"""You are tasked with developing a simplified library access system.
 A base class Member holds the basic member information like name and membership ID. 
 A subclass StudentMember allows book checkouts and displays the number of books currently borrowed.
 Implement necessary methods to add a book, return a book, and display borrowing status."""
class m:
    def _init_(self,n,i):
        self.n = n
        self.i = i
class s(m):
    def _init_(self,n,i):
        super()._init_(n,i)
        self.b=0
    
    def a(self):
         self.b += 1
    
    def r(self):
        if self.b>0:
            self.b-=1
    
    def s(self):
        print(f"{self.n}has{self.b}book(s).")
x=s("tom","c101")
x.a()
x.a()
x.s()
x.r()
x.s()
