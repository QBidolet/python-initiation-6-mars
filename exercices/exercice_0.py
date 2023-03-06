# Codez ici sans utilisez de nombre ni d'opérateur mathématique
# à part le  =
# pour obtenir le resultat que a soit égale à 6 et b égale à 5

a = 5
b = 6

# solution 1
temp = a
a = b
b = temp
print(a, b)

# solution pythonic
a, b = b, a