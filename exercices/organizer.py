import os
import shutil

# Vous devez construire un organisateur de fichier à partir de ce dictionnaire.
# Le programme scannera un dossier dans lequel il y a des fichiers (text, pdf ...)
# et devra créer le dossier correspondant au clé du dictionnaire, si durant le scan on trouve des fichiers il faudra les déplacer dans le dossier correspondant.
# Exemple : dans mon dossier il y a un fichier .pdf, le programme doit créer le dossier PDF et déplacer le fichier à l'intérieur

folder_dict = {
    "IMAGES": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", ".svg",
               ".heif", ".psd"],
    "VIDEOS": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng",
               ".qt", ".mpg", ".mpeg", ".3gp", ".mkv"],
    "DOCUMENTS": [".doc", ".pptx", ".docx", ".doc", ".xla"],
    "AUDIO": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3",
              ".msv", ".ogg", ".oga", ".raw", ".vox", ".wav", ".wma"],
    "PLAINTEXT": [".txt", ".in", ".out"],
    "PDF": [".pdf"],
    "XML": [".xml"],
    "EXE": [".exe"]
}

chemin = os.path.join(os.getcwd(), "a trier")

for nom_fichier in os.listdir(chemin):
    _, extension = os.path.splitext(nom_fichier)
    print(extension)
    for key, values in folder_dict.items():
        if extension in values:
           chemin_dossier = os.path.join(os.getcwd(), key)
           os.makedirs(chemin_dossier, exist_ok=True)
           chemin_element = os.path.join(chemin, nom_fichier)
           shutil.move(chemin_element, chemin_dossier)

for element in os.scandir(chemin):
    if element.is_file():
        _, extension = os.path.splitext(element.name)
        print(extension)
        for key, values in folder_dict.items():
            if extension in values:
                chemin_dossier = os.path.join(os.getcwd(), key)
                os.makedirs(chemin_dossier, exist_ok=True)
                chemin_element = os.path.join(chemin, element.name)
                shutil.move(chemin_element, chemin_dossier)

for folder, subfolders, files in os.walk(chemin):
    print(folder, subfolders, files)
    for file in files:
        chemin_element = os.path.join(folder, file)
        _, extension = os.path.splitext(file)
        for key, values in folder_dict.items():
            if extension in values:
                chemin_dossier = os.path.join(chemin, key)
                os.makedirs(chemin_dossier, exist_ok=True)
                shutil.move(chemin_element, chemin_dossier)