# noms de variable utilise snake_case
# TOUT ALPHABET SAUF -, @, !, ?, \, /, #
# un nom de variable ne doit pas commencer
# par un chiffre

ma_boite = 42
ma_boite_2 = ma_boite
print(ma_boite_2)
print(id(ma_boite))
print(id(ma_boite_2))
print(id(42))

ma_boite = 5
print(ma_boite, ma_boite_2)
print(id(ma_boite), id(ma_boite_2))

# nom de variables valides
# a
# a1
# a_b_c_________95
# _abc
# _1a

# nom de variables invalides
# 1
# 1a
# 1_