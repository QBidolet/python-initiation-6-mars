nom = "Quentin"
age = 29

# condition
if nom == "Julien":
    print("Hello")
elif age == 35:
    print(age)
else:
    print("Aucune des conditions n'a été rempli.")

# boucle for
for caractere in nom:
    print(caractere)

# print(enumerate(nom))
print("#"*25)
for index, element in enumerate(nom):
    print(index)
    print(element)

# range
for element in range(0, 30, 3):
    print(element)

# while
i = 0
while i < 3:
    print('hello')
    # break sort de la boucle
    # continue va à la prochaine itération
    i += 1