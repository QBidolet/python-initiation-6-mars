# Un tuple est une liste immuable.

# un tuple vide
mon_tuple = ()
print(type(mon_tuple))

# un élément
mon_tuple = (99, 12)
print(type(mon_tuple))

a = 1, 2
print(a, type(a))

def items():
    return 1, 2, 3

cle, valeur, bidule = items()
print(a, type(a))