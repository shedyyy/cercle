from Point import Point
import math

class Cercle:
        def __init__(self,rayon : float, centre : Point = None):
            self__rayon = rayon
            if centre !=None:
                self__centre = Point(0,0)
            else:
                self__centre = centre



        def __str__(self) :
            return f"Cercle de centre {self.__centre} et rayon {self.__rayon}"

        def diametre(self):
            return 2*self__rayon

