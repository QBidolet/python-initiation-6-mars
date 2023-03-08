from voiture import Voiture
from voiture_de_course import VoitureDeCourse

ma_voiture = Voiture("bleu", "Ford")
ferrari = VoitureDeCourse("Noir", "Ferrari", 300)
ferrari_2 = Voiture("Blanche", "Ferrari")
print(ferrari_2 == ferrari)