global a
a = 0
def une_fonction(un_nombre: int, une_chaine: str, un_float: float):
    a = 5


def une_autre_fonction():
    print(a)


une_fonction(5, 5.0, "5")
une_autre_fonction()
