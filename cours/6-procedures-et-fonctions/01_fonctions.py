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

