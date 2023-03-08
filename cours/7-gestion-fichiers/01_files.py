# 4 modes d'ouvertures
# w : pour écrire et écraser le contenu
# (crée le fichier si inexistant.)
# r : pour lire
# x : pour écrire seulement si le fichier est inexistant
# a : pour ajouter à suite.

fichier = open("mon_fichier.txt", "a")
fichier.write("Bonjour")
fichier.close()
with open('mon_fichier.txt', 'r') as fichier:
    contenu = fichier.read()

print(contenu)