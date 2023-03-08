class Voiture:
    def __init__(self, couleur, marque):
        self.couleur = couleur
        self.marque = marque

    def klaxonner(self):
        print("tut tut")

    def repeindre(self, couleur):
        self.couleur = couleur

    def __str__(self):
        return f"Je suis une voiture {self.marque}" \
               f" de couleur {self.couleur}."

    def __eq__(self, other):
        return self.marque == other.marque



ma_voiture = Voiture("Blanche", "Tesla")
ma_voiture_2 = Voiture("Noir", "Tesla")
print(ma_voiture == ma_voiture_2)

