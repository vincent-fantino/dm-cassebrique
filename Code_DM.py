import pyxel, random

# taille de la fenetre 256*256 pixels
pyxel.init(256, 256, title="DM_NSI")

# position initiale du plateau
# (origine des positions : coin haut gauche)
plateau_x = 112
plateau_y = 180

balle_x = 128
balle_y = 115

vitesse = 1

deplacement_vertical = 1
deplacement_horizontal = random.randint(-1,1)

vies = 3

vies_brique_1 = 2
vies_brique_2 = 3
vies_brique_3 = 1

bd1 = 0
bd2 = 0 
bd3 = 0

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

    global plateau_x, plateau_y, balle_y, balle_x, deplacement_vertical, deplacement_horizontal, vies, vitesse, bd1, bd2, bd3
     
    # mise à jour de la position du plateau et de la balle
    plateau_x, plateau_y = plateau_deplacement(plateau_x, plateau_y)

    balle_y = balle_y + deplacement_vertical 
    balle_x = balle_x + deplacement_horizontal 

    # rebonds

    if balle_x >= 256 : 
        deplacement_horizontal =-1*vitesse 
        
        
    if balle_x <= 0 : 
        deplacement_horizontal = 1*vitesse 
    
    if balle_y >= 256 :
        vies = vies - 1
        balle_y = 115
        balle_x = 128
        deplacement_horizontal = -1*vitesse or 0 or 1*vitesse 
        #random.randint(-1*vitesse,1*vitesse)

        
    if balle_y <= 0 :
        deplacement_vertical = 1*vitesse 
        
    if plateau_y <= balle_y <= plateau_y + 17 and plateau_x <= balle_x <=plateau_x + 32 :
        deplacement_vertical = -1*vitesse 
        
        
    if plateau_y <= balle_y <= plateau_y + 16  and plateau_x + 32 <= balle_x <=plateau_x + 32 + 16 :
        deplacement_vertical = -1*vitesse 
        if deplacement_horizontal == -1*vitesse or deplacement_horizontal == 0 :
            deplacement_horizontal = 1*vitesse 
        if deplacement_horizontal == 1*vitesse :
            deplacement_horizontal == 1*vitesse
        
    if plateau_y <= balle_y <= plateau_y + 16 and plateau_x - 14 <= balle_x <= plateau_x :
        deplacement_vertical = -1*vitesse 
        if deplacement_horizontal == 1 or deplacement_horizontal == 0 :
            deplacement_horizontal = -1*vitesse 
        if deplacement_horizontal == -1*vitesse :
            deplacement_horizontal == 1*vitesse
    
# =========================================================
# == DRAW
# =========================================================
def draw():
    """création des objets (30 fois par seconde)"""

    global plateau_x, plateau_y, balle_y, balle_x, deplacement_vertical, vies, vies_brique_1, vies_brique_2, vies_brique_3, deplacement_horizontal, vitesse, bd1, bd2, bd3
    
    if vies > 0 :
        
    # vide la fenetre
        pyxel.cls(0)
        
    # affichage des vies des briques
        if vies_brique_1 > 0 :
            pyxel.text(5,220,"brique de gauche "+str(vies_brique_1), 7)

        if vies_brique_2 > 0 :
            pyxel.text(96,220,"brique du milieu "+str(vies_brique_2), 7)

        if vies_brique_3 > 0 :
            pyxel.text(180,220,"brique de droite "+str(vies_brique_3), 7)
        
    # affichage des vies 
        pyxel.text(120,240,"vies "+str(vies), 7)
        
    # balle 
        pyxel.circ(balle_x, balle_y, 1, 8)

    # plateau 
        pyxel.rect(plateau_x, plateau_y, 32, 17, 6)
        pyxel.tri(plateau_x + 32, plateau_y, plateau_x + 32, plateau_y + 16, plateau_x + 32 + 16, plateau_y + 16, 6)
        pyxel.tri(plateau_x , plateau_y, plateau_x , plateau_y + 16, plateau_x - 16, plateau_y + 16, 6)

    # rebonds des briques
        # brique de gauche 
        if 24 <= balle_y <= 26 and 64-13 < balle_x < 64-13+26 and vies_brique_1 > 0 :
            vies_brique_1 = vies_brique_1 - 1
            deplacement_vertical = -1*vitesse 

        elif 25+16 <= balle_y <= 25+18 and 64-13 <= balle_x <= 64-13+26 and vies_brique_1 > 0 :
            vies_brique_1 = vies_brique_1 - 1
            deplacement_vertical = 1*vitesse 
            
        elif 24 <= balle_y <= 25+18 and 64-13+25 <= balle_x <= 64-13+27 and vies_brique_1 > 0 :
            vies_brique_1 = vies_brique_1 - 1
            deplacement_horizontal = - deplacement_horizontal
            
        elif 25 < balle_y < 25+17 and 64-13 <= balle_x <= 64-11 and vies_brique_1 > 0 :
            vies_brique_1 = vies_brique_1 - 1
            deplacement_horizontal = - deplacement_horizontal
        

        # brique du milieu
        if 24 <= balle_y <= 26 and 128-13 <= balle_x <= 128-13+26 and vies_brique_2 > 0 :
            vies_brique_2 = vies_brique_2 - 1
            deplacement_vertical = -1*vitesse 

        elif 25+16 <= balle_y <= 25+18 and 128-13 <= balle_x <= 128-13+26 and vies_brique_2 > 0 :
            vies_brique_2 = vies_brique_2 - 1
            deplacement_vertical = 1*vitesse 
            
        elif 25 <= balle_y <= 25+17 and 128-13+25 <= balle_x <= 128-13+27 and vies_brique_2 > 0 :
            vies_brique_2 = vies_brique_2 - 1
            deplacement_horizontal = - deplacement_horizontal
            
        elif 25 < balle_y < 25+17 and  128-14 <= balle_x <= 128-12 and vies_brique_2 > 0 :
            vies_brique_2 = vies_brique_2 - 1
            deplacement_horizontal = - deplacement_horizontal

        # brique de droite
        if 24 <= balle_y <= 26 and 192-13 < balle_x < 192-13+26 and vies_brique_3 > 0 :
            vies_brique_3 = vies_brique_3 - 1
            deplacement_vertical = -1*vitesse 

        elif 25+16 <= balle_y <= 25+18 and 192-13 < balle_x < 192-13+26 and vies_brique_3 > 0 :
            vies_brique_3 = vies_brique_3 - 1
            deplacement_vertical = 1*vitesse 
            
        elif 25 <= balle_y <= 25+17 and balle_x == 192-13+26 and vies_brique_3 > 0 :
            vies_brique_3 = vies_brique_3 - 1
            deplacement_horizontal = - deplacement_horizontal
            
        elif 25 < balle_y < 25+17 and balle_x == 192-13 and vies_brique_3 > 0 :
            vies_brique_3 = vies_brique_3 - 1
            deplacement_horizontal = - deplacement_horizontal

        # affichage des briques 
        if vies_brique_1 > 0 : 
            pyxel.rect(64-13, 25, 25, 17, 10)
        if vies_brique_1 == 0 and bd1 == 0:
            bd1 = 1
            vitesse = vitesse + 1
            print("vitesse +")
        
        if vies_brique_2 > 0 :
            pyxel.rect(128-13, 25, 25, 17, 10)
            
        if vies_brique_2 == 0 and bd2 == 0:
            bd2 = 1
            vitesse = vitesse + 1
            print("vitesse +")

        if vies_brique_3 > 0 : 
            pyxel.rect(192-13, 25, 25, 17, 10)
            
        if vies_brique_3 == 0 and bd3 == 0 :
            bd3 = 1
            vitesse = vitesse + 1
            print("vitesse +")
    # fins de jeu
    if vies == 0 :
        pyxel.cls(0)
        pyxel.text(120,128,"PERDU", 1)

    if vies_brique_1 == 0 and vies_brique_2 == 0 and vies_brique_3 == 0 :
        pyxel.cls(0)
        pyxel.text(120,128,"GAGNE", 1)



pyxel.run(update, draw)
