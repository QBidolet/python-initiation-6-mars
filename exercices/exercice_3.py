"""
Exercice3
Il faut créer un programme qui affiche les 20 premiers termes de la table de multiplication de 7
Bonus : Pouvoir rendre variable le nombre de termes et la table choisie
Utiliser des functions
"""
def generer_table_multiplication(nombre_terme, table):
    for element in range(1, nombre_terme+1):
        print(f"{table} X {element} = {table * element}")

generer_table_multiplication(20, 5)