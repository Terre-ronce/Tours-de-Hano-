from vpython import *
from hanoi import Hanoi
from utiles import resoudre, sequences

#  dimensions et titre
scene.width = 800
scene.height = 600
scene.title = "Simulation de la tour de Hanoï"

# création du jeu
hanoi = Hanoi(3)
hanoi.Assembler()

# nombre théorique d'opérations
operations_theoriques = 2 ** hanoi.nombre_anneaux - 1

# compteurs
texte_theorique = label(pos=vector(-hanoi.ecart_inter_tours, hanoi.hauteur + 3, 0), text=f"Nombres d'opérations théoriques : {operations_theoriques}", color=color.white)
texte_comptage = label(pos=vector(hanoi.ecart_inter_tours, hanoi.hauteur + 3, 0), text=f"Nombres d'opérations comptés : {hanoi.compteur_operations}", color=color.white)

resoudre(hanoi.nombre_anneaux, 'Tour1', 'Tour2', 'Tour3')
for sequence in sequences:
    hanoi.Deplacer_anneau(sequence[2], hanoi.elements[sequence[0]], texte_comptage)

# Validation finale
if hanoi.compteur_operations == operations_theoriques:
    texte_comptage.color = color.green
    texte_theorique.color = color.green
else:
    texte_comptage.color = color.red