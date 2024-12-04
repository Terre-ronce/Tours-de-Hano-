from vpython import *

class Tour:
    def __init__(self, rayon=0.2, hauteur=5, position=vector(0, 2.5, 0)):
        """
        Initialise la classe Tour.
        Arguments:
            rayon(float, optional): Le rayon du cylindre de la tour (par défaut 0.2).
            hauteur(float, optional): La hauteur du cylindre de la tour (par défaut 5).
            position(vector, optional): La position de la tour dans l'espace (par défaut (0, 2.5, 0)).
        """
        self.rayon = rayon
        self.hauteur = hauteur
        self.position = position
        self.obj = cylinder(pos=position - vector(0, hauteur / 2, 0), axis=vector(0, hauteur, 0), radius=rayon, texture=textures.metal)