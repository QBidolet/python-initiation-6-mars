from voiture import Voiture


class VoitureDeCourse(Voiture):
    def __init__(self, couleur, marque, vitesse="50"):
        Voiture.__init__(self, couleur, marque)
        self.vitesse = vitesse

    def __str__(self):
        return f"Je suis une voiture de course {self.marque}" \
               f" de couleur {self.couleur}" \
               f" et de vitesse {self.vitesse}."


tesla = VoitureDeCourse("Blanche", "Tesla", "300")
print(tesla)
