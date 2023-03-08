import os

# A ne pas faire : chemin absolu
chemin = "D:\python\mon-projet\mon-fichier.txt"


# Utiliser les chemins relatifs
chemin = os.path.join(os.getcwd(), "test.txt")

# vérifier l'existence d'un fichier
print(os.path.isfile(chemin))

# changer de répertoire courant
chemin_nouveau_repertoire = os.path.join(os.getcwd(), "data")
os.chdir(chemin_nouveau_repertoire)
print(os.getcwd())

# création d'un dossier
os.makedirs("Images", exist_ok=True)

# récupérer l'extension d'une fichier
nom, extension = os.path.splitext('fichier.py')
print(nom, extension)

# lister les dossiers et fichiers
print(os.listdir(os.getcwd()))

# walk pour parcourir avec un Iterable (le parcours est récursif)
for folder, sub_folders, files in os.walk(os.getcwd()):
    print(folder, sub_folders, files)

# scandir pour manipuler des DirEntry
for element in os.scandir(os.getcwd()):
    print(element)
    print(element.is_file())
    print(element.is_dir())