from vpython import *

class Socle:
    def __init__(self, longueur=10, largeur=4, epaisseur=0.5, position=vector(0, 0, 0)):
        """
        Initialise un objet Socle pour le socle du jeu.

        Argumentss:
            longueur (float, optional): La longueur du socle. Par défaut, 10.
            largeur (float, optional): La largeur du socle. Par défaut, 4.
            epaisseur (float, optional): L'épaisseur du socle. Par défaut, 0.5.
            position (vector, optional): La position du socle dans l'espace. Par défaut, vector(0, 0, 0).
        """
        self.longueur = longueur
        self.largeur = largeur
        self.epaisseur = epaisseur
        self.position = position
        self.obj = box(pos=position, size=vector(longueur, epaisseur, largeur), color=color.yellow, texture=textures.wood)