from vpython import *
from socle import Socle
from tour import Tour
from anneau import Anneau

class Hanoi:
    """
    Classe représentant le jeu de Hanoi.

    Attributes:
        nombre_anneaux (int): Le nombre d'anneaux dans le jeu.
        rayons (list): La liste des rayons des anneaux.
        hauteur (float): La hauteur totale du jeu.
        ecart_inter_tours (int): L'écart horizontal entre les tours.
        longueur (int): La longueur totale du jeu.
        compteur_operations (int): Le compteur d'opérations effectuées.

    Methods:
        Assembler(): Assemble les éléments du jeu.
        anneaux_sur_tour(): Retourne un dictionnaire contenant les anneaux présents sur chaque tour.
        Deplacer_anneau(tour: str, anneau: Anneau, texte_comptage): Déplace un anneau d'une tour à une autre.
    """

    def __init__(self, nombre_anneaux):
        """
        Initialise une instance de la classe Hanoi.

        Args:
            nombre_anneaux (int): Le nombre d'anneaux dans le jeu.
        """
        self.nombre_anneaux = nombre_anneaux
        self.rayons = list(range(1, self.nombre_anneaux+1))
        self.hauteur = nombre_anneaux * 0.2 + 3
        self.ecart_inter_tours = 2 * self.nombre_anneaux + 1
        self.longueur = 3 * self.ecart_inter_tours
        self.compteur_operations = 0

    def Assembler(self):
        """
        Assemble les éléments du jeu.
        """
        self.socle = Socle(longueur=self.longueur)
        self.Tour1 = Tour(hauteur= self.hauteur, position=vector(-self.ecart_inter_tours, self.hauteur / 2, 0))
        self.Tour2 = Tour(hauteur= self.hauteur, position=vector(0, self.hauteur / 2, 0))
        self.Tour3 = Tour(hauteur= self.hauteur, position=vector(self.ecart_inter_tours, self.hauteur / 2, 0))

        self.elements = {'Socle': self.socle,
                         'Tour1': self.Tour1,
                         'Tour2': self.Tour2,
                         'Tour3': self.Tour3}

        self.anneaux = []
        for i in range(self.nombre_anneaux):
            mod = self.nombre_anneaux - 1
            self.anneaux.append(Anneau(rayon=self.rayons[i], position=vector(-self.ecart_inter_tours, 0.45 + (mod - i) * 0.25, 0)))
        for i, elm in enumerate(self.anneaux):
            self.elements[f'Anneau{i +1}'] = elm

    @property
    def anneaux_sur_tour(self):
        """
        Retourne un dictionnaire contenant les anneaux présents sur chaque tour.

        Returns:
            dict: Un dictionnaire avec les tours comme clés et les anneaux comme valeurs.
        """
        dico = {'Tour1': [], 'Tour2': [], 'Tour3': []}
        for cle, obj in self.elements.items():
            if cle.startswith('Anneau'):
                if abs(obj.obj.pos.x - self.Tour1.obj.pos.x) < 0.1:
                    dico['Tour1'].append(obj)
                elif abs(obj.obj.pos.x - self.Tour2.obj.pos.x) < 0.1:
                    dico['Tour2'].append(obj)
                elif abs(obj.obj.pos.x - self.Tour3.obj.pos.x) < 0.1:
                    dico['Tour3'].append(obj)
        return dico

    def Deplacer_anneau(self, tour: str, anneau: Anneau, texte_comptage):
        """
        Déplace un anneau d'une tour à une autre.

        Args:
            tour (str): Le nom de la tour cible.
            anneau (Anneau): L'anneau à déplacer.
            texte_comptage (VPython.text): Le texte affichant le compteur d'opérations.
        """
        # position actuelle de l'anneau
        position_anneaux = anneau.obj.pos
        # position cible de la tour
        position_tour = self.elements[tour].obj.pos
        # hauteur du dernier anneau sur la tour cible
        y_dernier_anneau = self.anneaux_sur_tour[tour][0].obj.pos.y if self.anneaux_sur_tour[tour] else 0
        # hauteur de levée avant déplacement horizontal
        hauteur_levage = self.hauteur + 0.5

        # levage de l'anneau
        while position_anneaux.y < hauteur_levage:
            rate(50)
            position_anneaux.y += 0.1
            anneau.obj.pos = position_anneaux

        # déplacement horizontal vers la tour cible
        while abs(position_anneaux.x - position_tour.x) > 0.1:
            rate(50)
            position_anneaux.x += 0.1 if position_anneaux.x < position_tour.x else -0.1
            anneau.obj.pos = position_anneaux
        
        position_anneaux.x = position_tour.x
        anneau.obj.pos = position_anneaux

        # descente sur la pile de la tour cible
        while position_anneaux.y > y_dernier_anneau + 0.45:
            rate(50)
            position_anneaux.y -= 0.05
            anneau.obj.pos = position_anneaux

        # Incrémenter le compteur d'opérations
        self.compteur_operations += 1
        texte_comptage.text = f"Nombres d'opérations comptés : {self.compteur_operations}"
