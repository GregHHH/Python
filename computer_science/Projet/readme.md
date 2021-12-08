### Tout est possible,
### Tout est réalisable, 
# c'est  **LE JEU DE LA VIE!**

## Règles: 

Le jeu se déroule sur une grille à deux dimensions (matrice) dont les cases sont appelées « cellules », par analogie avec les cellules vivantes.

Chaque cellule peut  prendre deux états distincts : « **vivante** » ou « **morte** » (1 ou 0).

Une cellule possède **huit voisins**, qui sont les cellules adjacentes horizontalement, verticalement et diagonalement.

À chaque itération, l'état d’une cellule est entièrement déterminé par l’état de ses huit cellules voisines, selon les règles suivantes :
- une cellule **morte** possédant exactement trois cellules voisines vivantes devient vivante

- une cellule **vivante** possédant deux ou trois cellules voisines vivantes le reste, sinon elle meurt

---

## Utilisation du programme:

### Étape N°1: Géneration de la grille:

Pour commencer, il est nécéssaire de choisir la taille de notre grille. Pour cela, on utilise le fichier generate.py avec comme arguments le nombre de lignes, de colonnes et le pourcentage de cellules vivantes lors de la première itération:


```shell
python3 generate.py {nbr_lignes} {nbr_colonnes} {pourcentage}
```

```shell
python3 generate.py 8 2 40
```

⚠️ La valeur par defaut des lignes / colonnes est de **6** en l'absence de valeurs choisies en tant qu'arguments. 

⚠️ La valeur par defaut de la proportion de cellules vivantes est de **10%** en l'absence de valeurs choisies en tant qu'arguments.