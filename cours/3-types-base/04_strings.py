# escape avec \
ma_phrase = "J'ai mon masque."
ma_phrase = 'J\'ai mon masque.'

# combiner avec +
prenom = "Quentin"
nom = "BIDOLET"

# écrire la phrase suivante
# Je m'appelle Quentin BIDOLET.

# simple
ma_phrase = "Je m'appelle " + prenom + " " + nom + "."
print(ma_phrase)

# version python 2
ma_phrase = "Je m'appelle %s %s." % (prenom, nom)
print(ma_phrase)

# version python 3
ma_phrase = "Je m'appelle {0} {1}.".format(prenom, nom)
print(ma_phrase)

# version pythonic
ma_phrase = f"Je m'appelle {prenom} {nom}."
print(ma_phrase)

# dupliquer avec *
print("#" * 25)

# extraire avec []
alphabet = 'abcdefghij'
# [ start : end : step ]
print(alphabet[0])
print(alphabet[0:2])
# [0] prend le caractère à l'indice 0
# [:] prend toute la chaine
# [start :] démarre de l'indice donné jusqu'à la fin
print(alphabet[:])
print(alphabet[2:])
# [: end] du début jusqu'à l'indice donné
print(alphabet[:2])
# [ start : end ] d'indice à indice
print(alphabet[2:4])
# [start:end:step]
print(alphabet[::2])

print(alphabet[::-1])