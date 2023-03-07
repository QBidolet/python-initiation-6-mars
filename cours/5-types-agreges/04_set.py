# ensemble désordonnée sans doublon.

prenoms = {
    "Quentin",
    "Julien",
    "Romain"
}

prenoms.add("Frédéric")
print(prenoms)

prenoms.update(["Bénédicte", "Karine"])
print(prenoms)

prenoms.remove("Frédéric")
print(prenoms)

for element in prenoms:
    print(element)

if "Quentin" in prenoms:
    print("Quentin est présent.")

ma_liste = [1, 2, 2, 3, 5, 6, 6]
valeurs_uniques = set(ma_liste)
print(valeurs_uniques)