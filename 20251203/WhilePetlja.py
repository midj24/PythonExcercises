import random

tajmer = 5
while tajmer > 0:
    print(tajmer)
    tajmer -= 1

broj_pokusaja = 3
while broj_pokusaja > 0:
    print("Saljem zahtev za podatke")
    podaci = "Dobijeni podaci"
    if podaci != "":
        print(">> Podaci su dobijeni")
        print(">>> Napustam petlju")
        break
    else:
        broj_pokusaja -= 1
