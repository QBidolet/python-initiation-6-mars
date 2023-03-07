une_liste = ["pomme", "banane", "kiwi"]

print(type(une_liste))

une_liste = ["pomme", 1, 1.0, True, ["kiwi"], []]
print(une_liste)

print(une_liste[0], une_liste[4][0])

print("#" * 25)
print(une_liste[-2][0], une_liste[4][0])

print("#" * 25)
ma_liste = [1, 2, 3]
ma_liste.append(4)
print(ma_liste)
ma_liste.insert(0, -99)
print(ma_liste)
print(ma_liste.count(-99))

print(ma_liste)

del ma_liste[0]

print(ma_liste)

# gestion mémoire
a = [9, 8, 7, 5, 4, 3]
b = [a[2], a[5]]
print(b)
a[2] = 99
print(b)

print("#" * 25)
a = [9, 8, 7, 5, 4, 3]
b = a
a[0] = 99
print(a, b)

print('#' * 25)
ma_liste = ["pomme", "banane"]

# test d'appartenance
if "pomme" in ma_liste:
    print("Pomme est dans la liste !")

# parcours d'une liste
for element in ma_liste:
    print(element)

# trier
ma_liste = [5, 2, 3.14, -7]

# attention, cela change les indices.
# ma_liste.sort(reverse=True)
# print(ma_liste[0])
ma_liste.reverse()
print(ma_liste)

ma_liste_2 = ["Hello"]
ma_liste += ma_liste_2
ma_liste.sort()
print(ma_liste)