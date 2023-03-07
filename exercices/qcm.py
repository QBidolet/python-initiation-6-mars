question_1 = "Q1. Quel est le résultat du calcul : 4*6-2 ?" \
    "\n(a) 22" \
    "\n(b) 26" \
    "\n(c) 30" \
    "\n(d) Autre"

question_2 = "\nQ2. Quel est le résultat du calcul : 1+(2*4) ?" \
"\n(a) 1.5" \
"\n(b) 3" \
"\n(c) 3.5" \
"\n(d) Autre."

question_3 = "\nQ3. Un set peut contenir des valeurs dupliquées." \
"Cette phrase est :" \
"\n(a) Vraie" \
"\n(b) Fausse" \
"\n(c) Partiellement vraie" \
"\n(d) Autre."

questions = {
    question_1: "a",
    question_2: "b",
    question_3: "b"
}

print("Bienvenue sur le QCM.")
print("="*25)
score = 0
for question in questions:
    print(question)
    reponse = input("Tapez votre réponse (a/b/c/d)")
    if reponse == questions[question]:
        score += 1
else:
    print(f"\nVotre score : {score}/{len(questions)}")