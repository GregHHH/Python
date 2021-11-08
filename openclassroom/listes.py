def reset(title):
    print("\n")
    print("---------------------------------------------")
    print(title)
    print("---------------------------------------------")
    print("\n")


# ----------------------------------------------------------
# ----------------------------------------------------------
# ----------------------------------------------------------


fruits = ["pomme", "banane", "melon"]
print("contenu de la liste: ")
print(fruits)
print("\npremier élement de la liste = " + fruits[0])
print("second élement de la liste = " + fruits[1])
print("dernier élement de la liste = " + fruits[-1])

# s'applique de la meme facon pour les élements d'une string


# ----------------------------------------------------------
# ----------------------------------------------------------
# ----------------------------------------------------------


a = "partie 2: Modifier le contenu d'une liste"
reset(a)
fruits.append("poire")
print("\non ajouter un élément à la liste fruits:\n")
print(fruits)
fruits.remove("melon")
print("\nOn supprime l'élement 'melon' de la liste")
print(fruits)
print("\nOn trie la liste par ordre alphabétique: ")
fruits.sort()
print(fruits)

# ----------------------------------------------------------
# ----------------------------------------------------------
# ----------------------------------------------------------


a = "Partie 3: Les tuples"
reset(a)
print("Un tuple fonctionne de la méme facon qu'une liste mais ne peux pas être modifié. La syntax du tuple est la suivante: \n mon_tuple('e1','e2','e3')")

# ----------------------------------------------------------
# ----------------------------------------------------------
# ----------------------------------------------------------

