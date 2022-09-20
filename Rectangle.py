from Point import Point

class Rectangle :
    def __init__(self,longueur : float = 1, hauteur : float = 1,pbg : Point = Point(0,0),phd : Point = None):
        self.__pointBasGauche = pbg
        self.__longueur=longueur
        self.__hauteur=hauteur
        if phd!=None:
            self.__longueur = phd.get_x() - pbg.get_x()
            self.__hauteur = phd.get_y() - pbg.get_y()

    def __str__(self):
        return f"Rectangle de point bas gauche {self.__pointBasGauche}, de longueur {self.__longueur} et de hauteur {self.hauteur}"

    def surface(self):
        return self.__hauteur * self.__longueur

    def perimetre(self):
        return 2 * (self.__longueur + self.__hauteur)

    def getPointBasGauche(self):
        return self.__pointBasGauche

    def getPointBasDroit(self):
        p = Point(self.__pointBasGauche.get_x()+self.__longueur,self.__pointBasGauche.get_y())
        return p

    def getPointHautGauche(self):
        d = Point(self.__pointBasGauche.get_x(), self.__pointBasGauche.get_y() + self.__hauteur)
        return d

    def getPointHautDroit(self):
        c = Point(self.__pointBasGauche.get_x()+self.__longueur,self.__pointBasGauche.get_y() + self.__hautuer)
        return c