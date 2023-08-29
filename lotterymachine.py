import random

def losuj_element(lista):
    if len(lista) == 0:
        return None
    else:
        return random.choice(lista)

lista_elementow = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
wylosowany_element = losuj_element(lista_elementow)

if wylosowany_element is None:
    print("Lista jest pusta.")
else:
    print("Wylosowany element:", wylosowany_element)