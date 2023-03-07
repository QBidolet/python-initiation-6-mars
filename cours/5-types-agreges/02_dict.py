mon_dict = {
    "nom": "BIDOLET",
    "prenom": "Quentin",
}
print(type(mon_dict))
mon_dict["prenom"] = "Romain"
print(mon_dict["prenom"])

if "prenom" in mon_dict:
    print("oui")
else:
    print("non")

print(type(mon_dict.values()))
if "Romain" in mon_dict.values():
    print("La valeur est présente.")

if ('prenom', 'Romain') in mon_dict.items():
    print("La clé-valeur est présente.")

for element in liste:
    pass
for cle, valeur in mon_dict.items():
    print(cle, valeur

users = {
    "125aA": {
        "name": "BIDOLET"
    },
    "12515B": {
        "name": "DUPONT"
    }
}