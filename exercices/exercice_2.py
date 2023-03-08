"""
Écrivez un programme qui recherche le plus grand élément présent dans une liste donnée. Par exemple, si on l'appliquait à
la liste [32, 5, 12, 8, 3, 75, 2, 15],
ce programme devrait afficher : 75.
Bonus : ne pas utiliser la function max, min et avg de Python ( ni la function sort).
"""

liste = [1, 20, 3996, 4.1]
maximum = 0
if liste:
    for element in liste:
        if element > maximum:
            maximum = element
    else:
        print(maximum)
else:
    print("Veuillez rentrer une liste non vide.")
