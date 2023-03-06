# Fonction print
print("Hello World!")

# Séparateur
print("Hello", "World", sep="%")

# end
print("Hello", "World", sep="%", end="$$\n")

# On peut utiliser des guillemets simple
print('Hello World!')

# mettre une variable
print("Je suis {0} et {1}.".format("Quentin", "argument 2"))

# niveau 2
print("Je suis " + "Quentin et " + "argument 2.")

# échappement
print('J\'ai un escape.')

# Retour à la ligne
print("Ligne 1\nLigne 2")

# Plus simplement, on peut écrire
print("""Ligne 1
Ligne 2
""")

"""
Exercice : Afficher le texte suivant.
5-6$$$
7$$$
8
"""
print("5-6$$$\n7")
print("5-6", "7", sep="$$$\n")