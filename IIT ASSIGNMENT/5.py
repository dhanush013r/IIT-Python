"""Problem Statement: Develop a class ShapeCalculator to calculate areas.
 If one argument is passed, treat it as a circle radius and calculate the area. If two arguments are passed,
   treat them as length and width of a rectangle. Implement a single method area() with default parameters to simulate overloading.
 Ensure it returns appropriate outputs in each case."""
import math

class shapecalculator:
    def area(self,a=None,b=None):
          if a is not None and b is not None:
            return a*b 
          elif a is not None:
            return math.pi*a*a
          else:
            return "no dimensions provided"
        
