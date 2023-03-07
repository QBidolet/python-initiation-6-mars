def do_nothing():
    print("Elle s'execute !")


def somme(a, b, c):
    return a + b + c


# print(type(do_nothing))
# print(somme(1,))

def print_2(*args, sep=" ", end="\n"):
    for mot in args:
        print(mot, sep=sep, end=end)


print_2("Hello", "World", end="")


# unpacking
def items():
    return "cle", "valeur"


print("#" * 25)
print("#" * 25)
cle, valeur = items()
print(cle, valeur)


# **kwargs
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(key, value)


print("#" * 25)
print_kwargs(a=12, b=15, c=22, d=99)

print("#" * 25)


def somme(*args):
    resultat = 0
    for nombre in args:
        resultat += nombre
    return resultat


resultat = somme(1, 2, 3, 5, 6, 7)
print(resultat)

# fonctions anonymes
print("#" * 25)


def double(a):
    return a * 2


print(double(2))
liste = [1, 2, 3, 4]
# nouvelle_liste = []
# for nombre in liste:
#     nouvelle_liste.append(double(nombre))
# print(nouvelle_liste)

mon_map = map(double, liste)
print(list(mon_map))

mon_map = map(lambda x: x % 2, liste)
print(list(mon_map))

# filter
ma_liste = [6, 7, 8, 9]
nombres_pairs_filter_object = filter(lambda a: a % 2 == 0, ma_liste)
nombres_pairs = list(nombres_pairs_filter_object)


# closure
def fonction_externe(x):
    def fonction_interne(y):
        return x + y

    return fonction_interne

closure = fonction_externe(10)
print(fonction_externe(5))

print("#"*25)

# fonctions génératrices
def range(n):
    compteur = 0
    while compteur < n:
        compteur += 1
        yield compteur

for i in range(5):
    print(i)
