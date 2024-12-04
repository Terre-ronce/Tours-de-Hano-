from vpython import *

class Anneau:
    def __init__(self, rayon, epaisseur=0.2, position=vector(0, 0, 0), couleur=color.red):
        """
        Crée un objet Anneau.

        Args:
            rayon (float): Le rayon de l'anneau.
            epaisseur (float, optional): L'épaisseur de l'anneau. Par défaut 0.2.
            position (vector, optional): La position de l'anneau dans l'espace. Par défaut vector(0, 0, 0).
            couleur (color, optional): La couleur de l'anneau. Par défaut color.red.
        """
        self.rayon = rayon
        self.epaisseur = epaisseur
        self.position = position
        self.couleur = couleur
        self.obj = ring(pos=position, axis=vector(0, 1, 0), radius=rayon, thickness=epaisseur, color=couleur)