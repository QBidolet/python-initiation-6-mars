import os
import shutil

# copier un fichier dans un dossier
# pour renommer vous pouvez changer le nom de destination
# attention si le fichier existe déjà il sera écrasé
src = os.path.join(os.getcwd(), "test.txt")
dst = os.path.join(os.getcwd(), "data", 'test2.txt')
shutil.copy(src, dst)

# copie récursive
src = os.path.join(os.getcwd(), "data")
dst = os.path.join(os.getcwd(), "data_backup")
shutil.copytree(src, dst)

# suppression récursive
shutil.rmtree(dst)

# déplacement d'un dossier ou fichier
src = os.path.join(os.getcwd(), "test.txt")
dst = os.path.join(os.getcwd(), "data", "test_3.txt")
shutil.move(src, dst)
