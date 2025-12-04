#zadatak sa crtanje kvadrata
#iscrtajte kvadrat 3x3
#mozemo i da promenimo velicinu kvardata na 5x3
for x in range(3):
    for y in range(3):
        print("#", end="")
    print("")    

visina = 5
sirina = 10
for x in range(visina):
    for y in range(sirina):
        if x == 0 or x == 4 or y == 0 or y ==9:
            print("#", end="")
        else:
            print(" ", end="")
    print()
