"""
Un programme qui demande à l'utilisateur de saisir des noms de chats
et le programme se stop une fois que l'utilisateur décide d'arrêter la saisie et
doit nous retourner la liste des chats saisies dans l'ordre de saisie
Bonus : ne pas pouvoir saisir deux fois le même nom et afficher le numéro du chat à saisir ( example : saisir chat numéro 1 etc ... )
Votre programme doit gérer les exceptions de saisie
"""

chats = []
reponse = ""
mots_stop = ["stop", "exit", "quit", "quitter"]
while reponse not in mots_stop:
    reponse = input(f"Entrez un nom de chat n°{len(chats)+1}\n")
    reponse = reponse.strip().capitalize()
    if reponse.lower() in mots_stop:
        break
    try:
        if reponse == "":
            raise ValueError("Attention pas nom vide.")
    except ValueError as e:
        print(e)
    else:
        if reponse not in chats:
            chats.append(reponse)
        else:
            print(f"Vous avez déjà mis ce nom de chat ({reponse}).")

for index, nom_chat in enumerate(chats):
    print(f"Chat n°{index + 1} : {nom_chat}")