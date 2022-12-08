import pyxel, random

# taille de la fenetre 256*256 pixels
# ne pas modifier
pyxel.init(256, 256, title="DM_NSI")

# position initiale du vaisseau
# (origine des positions : coin haut gauche)
vaisseau_x = 112
vaisseau_y = 180

balle_x = 128
balle_y = 128

deplacement_vertical = 1
deplacement_horizontal = random.randint(-1,1)

vies = 3

vies_brique_1 = 2
vies_brique_2 = 3
vies_brique_3 = 1

def plateau_deplacement(x, y):
    """déplacement avec les touches de directions"""

    if pyxel.btn(pyxel.KEY_RIGHT):
        if (x < 256-32-14-2) :
            x = x + 2
    if pyxel.btn(pyxel.KEY_LEFT):
        if (x > 16) :
            x = x - 2
    return x, y

# =========================================================
# == UPDATE
# =========================================================
def update():
    """mise à jour des variables (30 fois par seconde)"""

    global vaisseau_x, vaisseau_y, balle_y, balle_x, deplacement_vertical, deplacement_horizontal, vies
     
    # mise à jour de la position du plateau et de la balle
    vaisseau_x, vaisseau_y = plateau_deplacement(vaisseau_x, vaisseau_y)

    balle_y = balle_y + deplacement_vertical 
    balle_x = balle_x + deplacement_horizontal 
    deplacement_vertical = deplacement_vertical 
    deplacement_horizontal = deplacement_horizontal 

    if balle_x >= 256 : 
        deplacement_horizontal =-1 #-1
        
        
    if balle_x <= 0 : 
        deplacement_horizontal = 1 #1 
    
    if balle_y >= 256 :
        vies = vies - 1
        balle_y = 128
        balle_x = 128
        deplacement_horizontal = random.randint(-1,1)

        
    if balle_y <= 0 :
        deplacement_vertical = 1 #1
        
    if vaisseau_y <= balle_y <= vaisseau_y + 17 and vaisseau_x <= balle_x <=vaisseau_x + 32 :
        deplacement_vertical = -1 #-1
        
        
    if vaisseau_y <= balle_y <= vaisseau_y + 16  and vaisseau_x + 32 <= balle_x <=vaisseau_x + 32 + 16 :
        deplacement_vertical = -1 #-1
        #deplacement_horizontal = -1 #1
        if deplacement_horizontal == -1 or deplacement_horizontal == 0 :
            deplacement_horizontal = 1 #-1  
        if deplacement_horizontal == 1 :
            deplacement_horizontal == 1
        
    if vaisseau_y <= balle_y <= vaisseau_y + 16 and vaisseau_x - 14 <= balle_x <= vaisseau_x :
        deplacement_vertical = -1 #-1
        if deplacement_horizontal == 1 or deplacement_horizontal == 0 :
            deplacement_horizontal = -1 #-1  
        if deplacement_horizontal == -1 :
            deplacement_horizontal == 1
    
# =========================================================
# == DRAW
# =========================================================
def draw():
    """création des objets (30 fois par seconde)"""

    global vaisseau_x, vaisseau_y, balle_y, balle_x, deplacement_vertical, vies, vies_brique_1, vies_brique_2, vies_brique_3, deplacement_horizontal
    
    if vies > 0 :
        
    # vide la fenetre
        pyxel.cls(0)
        
    # affichage des vies de la brique
        pyxel.text(5,220,"brique de gauche "+str(vies_brique_1), 7)
        pyxel.text(96,220,"brique du milieu "+str(vies_brique_2), 7)
        pyxel.text(180,220,"brique de droite "+str(vies_brique_3), 7)
        
    # affichage des vies 
        pyxel.text(120,240,"vies "+str(vies), 7)
        
    # balle 
        pyxel.circ(balle_x, balle_y, 1, 8)

    # plateau 
        pyxel.rect(vaisseau_x, vaisseau_y, 32, 17, 6)
        pyxel.tri(vaisseau_x + 32, vaisseau_y, vaisseau_x + 32, vaisseau_y + 16, vaisseau_x + 32 + 16, vaisseau_y + 16, 6)
        pyxel.tri(vaisseau_x , vaisseau_y, vaisseau_x , vaisseau_y + 16, vaisseau_x - 16, vaisseau_y + 16, 6)

    # briques
        #brique de gauche 
        if balle_y == 25 and 64-13 < balle_x < 64-13+26 and vies_brique_1 > 0 :
            vies_brique_1 = vies_brique_1 - 1
            deplacement_vertical = -1 #-1
            print(vies_brique_1)

        elif balle_y == 25+17 and 64-13 < balle_x < 64-13+26 and vies_brique_1 > 0 :
            vies_brique_1 = vies_brique_1 - 1
            deplacement_vertical = 1 #1
            print(vies_brique_1)
            
        elif 25 < balle_y < 25+17 and balle_x == 64-13+26 and vies_brique_1 > 0 :
            vies_brique_1 = vies_brique_1 - 1
            deplacement_horizontal = - deplacement_horizontal
            print(vies_brique_1)
            
        elif 25 < balle_y < 25+17 and balle_x == 64-13 and vies_brique_1 > 0 :
            vies_brique_1 = vies_brique_1 - 1
            deplacement_horizontal = - deplacement_horizontal
            print(vies_brique_1)
        

        #brique du milieu
        if balle_y == 25 and 128-13 <= balle_x <= 128-13+26 and vies_brique_2 > 0 :
            vies_brique_2 = vies_brique_2 - 1
            deplacement_vertical = -1 #-1
            print(vies_brique_2)

        elif balle_y == 25+17 and 128-13 < balle_x < 128-13+26 and vies_brique_2 > 0 :
            vies_brique_2 = vies_brique_2 - 1
            deplacement_vertical = 1 #1
            print(vies_brique_2)
            
        elif 25 < balle_y < 25+17 and balle_x == 128-13+26 and vies_brique_2 > 0 :
            vies_brique_2 = vies_brique_2 - 1
            deplacement_horizontal = - deplacement_horizontal
            print(vies_brique_2)
            
        elif 25 < balle_y < 25+17 and balle_x == 128-13 and vies_brique_2 > 0 :
            vies_brique_2 = vies_brique_2 - 1
            deplacement_horizontal = - deplacement_horizontal
            print(vies_brique_2)

        #brique de droite
        if balle_y == 25 and 192-13 < balle_x < 192-13+26 and vies_brique_3 > 0 :
            vies_brique_3 = vies_brique_3 - 1
            deplacement_vertical = -1 #-1
            print(vies_brique_3)

        elif balle_y == 25+17 and 192-13 < balle_x < 192-13+26 and vies_brique_3 > 0 :
            vies_brique_3 = vies_brique_3 - 1
            deplacement_vertical = 1 #1
            print(vies_brique_3)
            
        elif 25 < balle_y < 25+17 and balle_x == 192-13+26 and vies_brique_3 > 0 :
            vies_brique_3 = vies_brique_3 - 1
            deplacement_horizontal = - deplacement_horizontal
            print(vies_brique_3)
            
        elif 25 < balle_y < 25+17 and balle_x == 192-13 and vies_brique_3 > 0 :
            vies_brique_3 = vies_brique_3 - 1
            deplacement_horizontal = - deplacement_horizontal
            print(vies_brique_3)

        # affichage des briques 
        if vies_brique_1 > 0 : 
            pyxel.rect(64-13, 25, 25, 17, 10) 
        
        if vies_brique_2 > 0 :
            pyxel.rect(128-13, 25, 25, 17, 10)

        if vies_brique_3 > 0 : 
            pyxel.rect(192-13, 25, 25, 17, 10)

    #fin de jeu
    if vies == 0 :
        pyxel.cls(0)
        pyxel.text(120,128,"PERDU", 1)

    if vies_brique_1 == 0 and vies_brique_2 == 0 and vies_brique_3 == 0 :
        pyxel.cls(0)
        pyxel.text(120,128,"GAGNE", 1)
""



pyxel.run(update, draw)

