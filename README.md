# Tours de Hanoï

Ce projet consiste à simuler en 3D la résolution récursive du jeu Tours de Hanoï dans le cas particulier où les anneaux sont sur une tour au début.

Pour la simulation on utilisera `vpython` [[1]](https://vpython.org/contents/doc.html) et pour la résolution ainsi que les règles, on se réfèrera à la page Wikipédia du jeu [[2]](https://fr.wikipedia.org/wiki/Tours_de_Hano%C3%AF).

Le résultat final pour une simulation à 3 anneaux se présente comme suit (vidéo accélérée):

<p align="center">
  <img src="https://github.com/user-attachments/assets/850788c3-645f-43e0-85f5-c3dbad096389" alt="animation" />
</p>

## Règles du jeu

### Le départ

On dispose de 3 piquets fixés sur un socle, et d'un nombre n de disques de diamètres différents. Les disques sont empilés sur un piquet, en commençant du plus large au plus petit.
Le nombre de disques peut varier. Plus il y a de disques au départ, plus le jeu est difficile.

### Le but

Déplacer les disques d'une tour de 'départ' à une tour 'd'arrivée' en passant par une tour 'intermédiaire', et ceci en un minimum de coups.

### Comment

2 règles simples :

- on ne déplace qu’un seul disque à la fois, et le disque déplacé doit l'être sur l’un des deux autres piquets au choix ; c’est ce que l’on appelle un déplacement.

- le disque déplacé ne doit jamais être placé au-dessus d’un disque plus petit que lui [[3]](https://jeux-casse-tete.com/blog/regles-de-jeux/regle-du-jeu-la-tour-de-hanoi-).

## Simulation

Pour la simulation on crée différents objets correspondants aux différents composants du jeu:

- `Socle`, objet créé avec `box` de `vpython` et permet de créer le socle du jeu ;
- `Tour`, objet créé avec `cylinder` de `vpython` et permet de créer les tours ;
- `Anneau`, objet créé avec `ring` de `vpython` et permet de créer les anneaux du jeu ;
- `Hanoi`, qui permet de réaliser l'assemblage pour former le set.

On peut alors implémenter l'algorithme récursif [[2]](https://fr.wikipedia.org/wiki/Tours_de_Hano%C3%AF#:~:text=section%20R%C3%A9solution%20algorithmique-,Solution%20r%C3%A9cursive,-Algorithme%20g%C3%A9n%C3%A9ralis%C3%A9%20%C3%A0) et ainsi créer des séquences de déplacement qui vont permettre de bouger les anneaux d'une tour vers une autre.

On affiche ensuite la comparaison entre le nombre minimal théoriques de déplacements, $2^n - 1$ (avec $n$ le nombre d'anneaux) et le nombre de déplacements éffectués lors de la simulation pour s'assurer de la concordance théorie/simulation.

## Références

[1]: Documentation for Classic VPython 6. VPython.

[2]: Tours de Hanoï. Wikipédia.

[3]: Règle du jeu : La Tour de Hanoï. Jeux casse-tête.
