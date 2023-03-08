ma_liste = ["Quentin", "Julien", "Maximilien"]

liste_sup_6 = []
liste_inf_6 = []

# for element in ma_liste:
#     if len(element) > 6:
#         liste_sup_6.append(element)
#     else:
#         liste_inf_6.append(element)
#

liste_sup_6 = [element for element in ma_liste if len(element) > 6]
liste_inf_6 = [element for element in ma_liste if len(element) <= 6]
print(liste_sup_6)

liste_avec_10_premier_nombre_pair_au_carre = \
    [element ** 2 for element in range(0, 20) if element % 2 == 0]
print(liste_avec_10_premier_nombre_pair_au_carre)

liste_avec_10_premier_nombre_pair_au_carre_et_double_impairs = \
    [element ** 2 if element % 2 == 0 else element * 2 for element in range(0, 20)]
