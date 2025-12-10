def ispisi_poruku(korisnicko_ime="gost"): # funkcija sa opcionim parametrom
    print(f"Zdravo {korisnicko_ime}!!!!")

ispisi_poruku(korisnicko_ime="Milos")
ispisi_poruku()

# def saberi(prvi_sabirak=0, drugi_sabirak=0):
#     print(prvi_sabirak + drugi_sabirak)

# #saberi(prvi_sabirak = 10, drugi_sabirak = 20)
# saberi()


def dodaj_oglas(naziv, cena, dodatne_informacije=""):
    print(f"Naziv: {naziv}")
    print(f"Cena: {cena}")
    if dodatne_informacije != "":
        print(f"Dodatne informacije: {dodatne_informacije}")

dodaj_oglas("Patike", 200)
dodaj_oglas("Automobil", 5000, "U odlicnom stanju")
dodaj_oglas(cena=520, naziv="Jakna", dodatne_informacije="Informacije o jakni.....")


brojevi = [5, 3, 4]
broj_clanova = len(brojevi)
print(broj_clanova)



def pomnozi(broj1,broj2):
    rezultat = broj1 * broj2
    return rezultat

rezultat_mnozenja=pomnozi(5,3)
print(rezultat_mnozenja)