# NOTE : Erreur ligne 61, if incomplet 

from re import M
from time import monotonic
import pyxel

# taille de la fenetre 128x128 pixels
# ne pas modifier
pyxel.init(256, 256, title="Nuit du code")

# position initiale du vaisseau
# (origine des positions : coin haut gauche)
vaisseau_x = 120
vaisseau_y = 180

balle_x = 50
balle_y = 50

class Point2D:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

class Hitbox:
    def __init__(self, p1 : Point2D, p2 : Point2D) -> None:
        self.p1 = p1
        self.p2 = p2
    @classmethod
    def collision(cls, rect1, rect2) -> bool:
        return (rect1.p1.x <= rect2.p2.x and rect2.p1.x <= rect1.p2.x) or (rect1.p1.y <= rect2.p2.y and rect2.p1.y <= rect1.p2.y)

balle = Hitbox(Point2D(balle_x, balle_y), Point2D(balle_x + 10, balle_y + 10))
plateau = Hitbox(Point2D(vaisseau_x, vaisseau_y), Point2D(vaisseau_x + 32, vaisseau_y + 17))



def plateau_deplacement(x, y):
    """déplacement avec les touches de directions"""

    if pyxel.btn(pyxel.KEY_RIGHT):
        if (x < 256-32-14) :
            x = x + 1
    if pyxel.btn(pyxel.KEY_LEFT):
        if (x > 14) :
            x = x - 1
    return x, y



# =========================================================
# == UPDATE
# =========================================================
def update():
    """mise à jour des variables (30 fois par seconde)"""

    global vaisseau_x, vaisseau_y, balle_y
     
    # mise à jour de la position du plateau
    vaisseau_x, vaisseau_y = plateau_deplacement(vaisseau_x, vaisseau_y)
    
    #if Hitbox.collision(balle, plateau) == True :
        

# =========================================================
# == DRAW
# =========================================================
def draw():
    """création des objets (30 fois par seconde)"""

    # vide la fenetre
    pyxel.cls(0)

    #balle 
    pyxel.circ(balle_x, balle_y, 5, 1)

    # plateau 
    pyxel.rect(vaisseau_x, vaisseau_y, 32, 17, 1)
    pyxel.tri(vaisseau_x + 32, vaisseau_y, vaisseau_x + 32, vaisseau_y + 16, vaisseau_x + 32 + 16, vaisseau_y + 16, 1)
    pyxel.tri(vaisseau_x , vaisseau_y, vaisseau_x , vaisseau_y + 16, vaisseau_x - 16, vaisseau_y + 16, 1)

    #briques
    pyxel.rect(25, 25, 25, 17, 1)





pyxel.run(update, draw)

#Exemple de class hitbox :

class Point2D:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

class Hitbox:
    def __init__(self, p1 : Point2D, p2 : Point2D) -> None:
        self.p1 = p1
        self.p2 = p2
    @classmethod
    def collision(cls, rect1, rect2) -> bool:
        return rect2.p1.y <= rect1.p2.y and rect1.p1.y <= rect2.p2.y or rect2.p1.x <= rect1.p2.x and rect2.p1.x <= rect1.p2.x

M = Point2D(1, 3)
N = Point2D(3, 5)
O = Point2D(2, 4)
P =Point2D(4, 6)

MN = Hitbox(M, N)
OP = Hitbox(O, P)

print(M)
print(N)
