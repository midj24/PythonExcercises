class Korisnik:
    korisnicko_ime = ""
    sifra = ""
    smer = ""
    godina_upisa = 0
    ustanova = "ITAcademy"
    krediti = 0

    def __init__(self, korisnicko_ime, sifra, smer, godina_upisa):
        self.korisnicko_ime = korisnicko_ime
        self.sifra = sifra
        self.smer = smer
        self.godina_upisa = godina_upisa

    def promeni_smer(self, novi_smer):
        print("Korisnik je promenio smer")
        self.smer = novi_smer
    def dodaj_kredite(self, vrednost):
        self.krediti = vrednost

    def prikazi_kredite(self):
        return self.krediti

korisnik1 = Korisnik("Milos", "123", "QA", 2025)
print(korisnik1.korisnicko_ime)
print(korisnik1.sifra)
print(korisnik1.smer.upper())
print(korisnik1)

recnik_korisnik = korisnik1.__dict__ # ovo je sada recnik nije vise instanca
for kljuc, vrednost in recnik_korisnik.items():
    print(kljuc, vrednost)

korisnik1.promeni_smer("Python")
print(korisnik1.smer)

korisnik2 = Korisnik("Petar", "543", "QA", 2025)
korisnik3 = Korisnik("Jovana", "789", "QA", 2024)

upisani_qa_korisnici = [korisnik1, korisnik2, korisnik3]
for korisnik in upisani_qa_korisnici:
    if korisnik.godina_upisa == 2025 and korisnik.smer == "QA":
        print("Ocekivano - 2025 QA")
    else:
        print(f"Greska - Korisnik je smer: {korisnik.smer}, godina upisa je: {korisnik.godina_upisa}")

# print(Korisnik.ustanova())

korisnik1.dodaj_kredite(50)
print(korisnik1.krediti)
print(korisnik2.krediti)
print(korisnik1.prikazi_kredite())


