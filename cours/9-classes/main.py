# from voiture import Voiture
# from voiture_de_course import VoitureDeCourse
#
# ma_voiture = Voiture("bleu", "Ford")
# ferrari = VoitureDeCourse("Noir", "Ferrari", 300)
# ferrari_2 = Voiture("Blanche", "Ferrari")
# print(ferrari_2 == ferrari)

from compte_bancaire import CompteBancaire

compte_1 = CompteBancaire("BIDOLET", 2150)
compte_1.deposer(1000)
compte_1.retrait(1000)
print(compte_1.nom, compte_1.solde)