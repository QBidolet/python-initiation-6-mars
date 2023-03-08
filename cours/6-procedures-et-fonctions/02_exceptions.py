# Lever une exception
# nombre = input("Entrez un nombre : ")
# nombre = int(nombre)
# print(nombre)

# Gérer l'exception
# nombre = input("Entrez un nombre : ")
# try:
#     nombre = int(nombre)
# except ValueError:
#     print("Veuillez rentrer un nombre valide.")

# Double exception
# try:
#     numerateur = int(input('Entrez un numérateur : '))
#     denominateur = int(input('Entrez un dénominateur : '))
#     resultat = numerateur / denominateur
# except ValueError as error:
#     print("Veuillez rentrer un nombre valide.")
#     print(error)
# except ZeroDivisionError:
#     print("La division par zéro n'est pas possible.")
# else:
#     print("Le résultat de la division est ", resultat)

# Lever exception
try:
    x = int(input("Saisissez un nombre positif."))
    if x < 0:
        raise ValueError("La valeur ne peut pas être négative.")
except ValueError as e:
    print(e)