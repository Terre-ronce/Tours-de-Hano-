# liste des séquences
sequences = []

def resoudre(nombre_anneaux, tour_debut, tour_milieu, tour_fin):
    """
    Résout le problème des tours de Hanoi avec la méthode récursive.

    Arguments:
        nombre_anneaux (int): Le nombre d'anneaux à déplacer.
        tour_debut (str): Le nom de la tour de départ.
        tour_milieu (str): Le nom de la tour intermédiaire.
        tour_fin (str): Le nom de la tour d'arrivée.
    
    Retours:
        Aucun
    """
    global sequences
    if nombre_anneaux == 1:
        sequences.append((f'Anneau{nombre_anneaux}', tour_debut, tour_fin))
    else:
        resoudre(nombre_anneaux - 1, tour_debut, tour_fin, tour_milieu)
        sequences.append((f'Anneau{nombre_anneaux}', tour_debut, tour_fin))
        resoudre(nombre_anneaux - 1, tour_milieu, tour_debut, tour_fin)