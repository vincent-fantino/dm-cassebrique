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
deplacement_vertical = 1



def plateau_deplacement(x, y):
    """déplacement avec les touches de directions"""

    if pyxel.btn(pyxel.KEY_RIGHT):
        if (x < 256-32-14-2) :
            x = x + 1
    if pyxel.btn(pyxel.KEY_LEFT):
        if (x > 16) :
            x = x - 1
    return x, y



# =========================================================
# == UPDATE
# =========================================================
def update():
    """mise à jour des variables (30 fois par seconde)"""

    global vaisseau_x, vaisseau_y, balle_y, balle_x, deplacement_vertical
     
    # mise à jour de la position du plateau
    vaisseau_x, vaisseau_y = plateau_deplacement(vaisseau_x, vaisseau_y)
    
        
    balle_y = balle_y + deplacement_vertical
    
    if balle_y + 5 == 256 :
        balle_y = 128
        balle_x = 128
        
    if balle_y == 0
        deplacement_vertical = 1
        
    if balle_y == vaisseau_y and vaisseau_x <= balle_x <=vaisseau_x + 32 :
        deplacement_vertical = -1
    
# =========================================================
# == DRAW
# =========================================================
def draw():
    """création des objets (30 fois par seconde)"""
    global vaisseau_x, vaisseau_y, balle_y, balle_x,deplacement_vertical
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
